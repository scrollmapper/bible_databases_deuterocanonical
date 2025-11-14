"""
Link crawler spider that follows links recursively.
"""
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..mixins import SignalAwareSpiderMixin


class CrawlLinkSpider(SignalAwareSpiderMixin, CrawlSpider):
    """
    Spider that crawls pages by following links.
    """
    name = 'crawl'
    
    rules = (
        Rule(LinkExtractor(), callback='parse_item', follow=True),
    )
    
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if url:
            self.start_urls = [url]
            # Extract domain from URL for allowed_domains
            from urllib.parse import urlparse
            parsed = urlparse(url)
            self.allowed_domains = [parsed.netloc]
        else:
            self.start_urls = []
            self.allowed_domains = []
    
    def parse_item(self, response):
        """
        Parse each crawled page.
        """
        yield {
            'url': response.url,
            'status': response.status,
            'title': response.css('title::text').get(),
            'links': len(response.css('a::attr(href)').getall()),
        }
