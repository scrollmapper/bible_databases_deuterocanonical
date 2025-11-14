"""
Custom logic spider for user-defined crawling behavior.
"""
import scrapy
from ..mixins import SignalAwareSpiderMixin


class CustomSpider(SignalAwareSpiderMixin, scrapy.Spider):
    """
    Spider with customizable logic.
    Users can extend this for specific use cases.
    """
    name = 'custom'
    
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if url:
            self.start_urls = [url]
        else:
            self.start_urls = []
    
    def parse(self, response):
        """
        Custom parsing logic.
        Override this method to implement specific behavior.
        """
        yield {
            'url': response.url,
            'status': response.status,
            'title': response.css('title::text').get(),
            'headers': dict(response.headers),
        }
