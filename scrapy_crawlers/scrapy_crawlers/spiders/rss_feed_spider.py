"""
RSS feed reader spider.
"""
import scrapy
from ..mixins import SignalAwareSpiderMixin


class RSSFeedSpider(SignalAwareSpiderMixin, scrapy.Spider):
    """
    Spider for reading and parsing RSS feeds.
    """
    name = 'rss'
    
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if url:
            self.start_urls = [url]
        else:
            self.start_urls = []
    
    def parse(self, response):
        """
        Parse RSS feed.
        """
        # Parse RSS items
        for item in response.xpath('//item'):
            yield {
                'title': item.xpath('title/text()').get(),
                'link': item.xpath('link/text()').get(),
                'description': item.xpath('description/text()').get(),
                'pubDate': item.xpath('pubDate/text()').get(),
            }
        
        # Also try Atom format
        for entry in response.xpath('//entry'):
            yield {
                'title': entry.xpath('title/text()').get(),
                'link': entry.xpath('link/@href').get(),
                'summary': entry.xpath('summary/text()').get(),
                'updated': entry.xpath('updated/text()').get(),
            }
