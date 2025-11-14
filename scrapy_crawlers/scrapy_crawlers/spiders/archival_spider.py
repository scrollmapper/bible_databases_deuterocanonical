"""
Archive crawler spider for archived pages.
"""
import scrapy
from ..mixins import SignalAwareSpiderMixin


class ArchivalSpider(SignalAwareSpiderMixin, scrapy.Spider):
    """
    Spider designed for crawling archived web pages.
    Can be used with archive.org or similar services.
    """
    name = 'archival'
    
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if url:
            self.start_urls = [url]
        else:
            self.start_urls = []
    
    def parse(self, response):
        """
        Parse archived page.
        """
        yield {
            'url': response.url,
            'status': response.status,
            'title': response.css('title::text').get(),
            'archive_date': response.headers.get('Memento-Datetime', b'').decode('utf-8'),
            'content_length': len(response.body),
        }
