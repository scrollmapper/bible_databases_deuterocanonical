"""
Link extractor spider that extracts all links from a page.
"""
import scrapy
from ..mixins import SignalAwareSpiderMixin


class LinkExtractorSpider(SignalAwareSpiderMixin, scrapy.Spider):
    """
    Spider that extracts all links from a page without following them.
    """
    name = 'link_extractor'
    
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if url:
            self.start_urls = [url]
        else:
            self.start_urls = []
    
    def parse(self, response):
        """
        Extract all links from the page.
        """
        links = response.css('a::attr(href)').getall()
        
        yield {
            'url': response.url,
            'status': response.status,
            'total_links': len(links),
            'links': links,
        }
