"""
Basic spider for simple page fetching.
"""
import scrapy
from ..mixins import SignalAwareSpiderMixin


class BasicSpider(SignalAwareSpiderMixin, scrapy.Spider):
    """
    Basic fetcher spider that retrieves a single page.
    """
    name = 'basic'
    
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if url:
            self.start_urls = [url]
        else:
            self.start_urls = []
    
    def parse(self, response):
        """
        Parse the response and yield basic page data.
        """
        yield {
            'url': response.url,
            'status': response.status,
            'title': response.css('title::text').get(),
            'content_length': len(response.body),
        }
