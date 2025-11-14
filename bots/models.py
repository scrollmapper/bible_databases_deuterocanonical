from django.db import models


class Bot(models.Model):
    """
    Model representing a web crawler bot with configurable settings.
    """
    CRAWLER_TYPE_CHOICES = [
        ('basic', 'Basic Fetcher'),
        ('crawl', 'Link Crawler'),
        ('sitemap', 'Sitemap Crawler'),
        ('api', 'API Harvester'),
        ('rss', 'RSS Feed Reader'),
        ('csv_feed', 'CSV Feed Processor'),
        ('json_feed', 'JSON Feed Processor'),
        ('link_extractor', 'Link Extractor'),
        ('archival', 'Archive Crawler'),
        ('darknet', 'Dark Web Crawler'),
        ('custom', 'Custom Logic Spider'),
    ]
    
    name = models.CharField(max_length=255, unique=True)
    crawler_type = models.CharField(
        max_length=50, 
        choices=CRAWLER_TYPE_CHOICES, 
        default='basic'
    )
    
    # Settings
    user_agent = models.CharField(
        max_length=500,
        default='MyBot (+http://example.com)',
        help_text='User agent string for the bot'
    )
    download_delay = models.FloatField(
        default=2.0,
        help_text='Delay in seconds between requests'
    )
    concurrent_requests = models.IntegerField(
        default=4,
        help_text='Maximum number of concurrent requests'
    )
    obey_robots_txt = models.BooleanField(
        default=True,
        help_text='Whether to obey robots.txt'
    )
    autothrottle_enabled = models.BooleanField(
        default=True,
        help_text='Enable auto-throttle extension'
    )
    cookies_enabled = models.BooleanField(
        default=False,
        help_text='Enable cookies'
    )
    
    # Statistics (read-only)
    last_run_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text='Last time this bot was run'
    )
    pages_fetched = models.IntegerField(
        default=0,
        help_text='Total number of pages fetched'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return f"{self.name} ({self.get_crawler_type_display()})"
