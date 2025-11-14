"""
Django management command for running Scrapy crawlers.
"""
import os
import subprocess
from datetime import datetime
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from bots.models import Bot


class Command(BaseCommand):
    help = 'Run a Scrapy crawler with settings from Bot model'
    
    def add_arguments(self, parser):
        parser.add_argument(
            'bot',
            type=int,
            help='Bot ID to use for crawling'
        )
        parser.add_argument(
            'url',
            type=str,
            help='Target URL to crawl'
        )
        parser.add_argument(
            '--crawler-type',
            type=str,
            help='Override crawler type (defaults to bot.crawler_type)',
            required=False
        )
    
    def handle(self, *args, **options):
        bot_id = options['bot']
        url = options['url']
        crawler_type = options.get('crawler_type')
        
        # Load Bot from database
        try:
            bot = Bot.objects.get(pk=bot_id)
        except Bot.DoesNotExist:
            raise CommandError(f'Bot with ID {bot_id} does not exist')
        
        # Use bot's crawler_type if not overridden
        if not crawler_type:
            crawler_type = bot.crawler_type
        
        # Validate crawler type
        valid_types = [choice[0] for choice in Bot.CRAWLER_TYPE_CHOICES]
        if crawler_type not in valid_types:
            raise CommandError(
                f'Invalid crawler type: {crawler_type}. '
                f'Valid types are: {", ".join(valid_types)}'
            )
        
        self.stdout.write(
            self.style.SUCCESS(
                f'Starting {crawler_type} crawler for bot "{bot.name}" on {url}'
            )
        )
        
        # Build Scrapy command with settings
        scrapy_dir = os.path.join(
            os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))),
            'scrapy_crawlers'
        )
        
        cmd = [
            'scrapy', 'crawl', crawler_type,
            '-a', f'url={url}',
            '-s', f'USER_AGENT={bot.user_agent}',
            '-s', f'DOWNLOAD_DELAY={bot.download_delay}',
            '-s', f'CONCURRENT_REQUESTS={bot.concurrent_requests}',
            '-s', f'ROBOTSTXT_OBEY={bot.obey_robots_txt}',
            '-s', f'AUTOTHROTTLE_ENABLED={bot.autothrottle_enabled}',
            '-s', f'COOKIES_ENABLED={bot.cookies_enabled}',
        ]
        
        # Run Scrapy crawler
        try:
            result = subprocess.run(
                cmd,
                cwd=scrapy_dir,
                capture_output=True,
                text=True,
                check=False
            )
            
            if result.returncode == 0:
                self.stdout.write(self.style.SUCCESS('Crawl completed successfully'))
                self.stdout.write(result.stdout)
                
                # Update bot statistics
                bot.last_run_at = timezone.now()
                bot.pages_fetched += 1  # Simple increment, could be enhanced
                bot.save()
            else:
                self.stdout.write(self.style.ERROR('Crawl failed'))
                self.stdout.write(self.style.ERROR(result.stderr))
                raise CommandError(f'Scrapy command failed with return code {result.returncode}')
                
        except FileNotFoundError:
            raise CommandError(
                'Scrapy command not found. Make sure Scrapy is installed and in PATH.'
            )
        except Exception as e:
            raise CommandError(f'Error running crawler: {str(e)}')
