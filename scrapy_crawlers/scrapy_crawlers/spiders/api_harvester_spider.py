"""
API harvester spider for JSON APIs.
"""
import scrapy
import json
from ..mixins import SignalAwareSpiderMixin


class APIHarvesterSpider(SignalAwareSpiderMixin, scrapy.Spider):
    """
    Spider designed to harvest data from JSON APIs.
    """
    name = 'api'
    
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if url:
            self.start_urls = [url]
        else:
            self.start_urls = []
    
    def parse(self, response):
        """
        Parse JSON API response.
        """
        try:
            data = json.loads(response.text)
            yield {
                'url': response.url,
                'status': response.status,
                'data': data,
                'data_type': type(data).__name__,
            }
        except json.JSONDecodeError as e:
            self.logger.error(f"JSON decode error: {e}")
            yield {
                'url': response.url,
                'status': response.status,
                'error': str(e),
            }
