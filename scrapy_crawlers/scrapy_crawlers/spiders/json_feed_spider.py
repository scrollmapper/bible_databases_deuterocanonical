"""
JSON feed processor spider.
"""
import scrapy
import json
from ..mixins import SignalAwareSpiderMixin


class JSONFeedSpider(SignalAwareSpiderMixin, scrapy.Spider):
    """
    Spider for processing JSON feeds.
    """
    name = 'json_feed'
    
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if url:
            self.start_urls = [url]
        else:
            self.start_urls = []
    
    def parse(self, response):
        """
        Parse JSON feed and yield each item.
        """
        try:
            data = json.loads(response.text)
            
            # If data is a list, yield each item
            if isinstance(data, list):
                for item in data:
                    yield {
                        'url': response.url,
                        'item': item,
                    }
            # If data is a dict, yield the whole thing
            else:
                yield {
                    'url': response.url,
                    'data': data,
                }
        except json.JSONDecodeError as e:
            self.logger.error(f"JSON decode error: {e}")
            yield {
                'url': response.url,
                'error': str(e),
            }
