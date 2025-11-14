"""
CSV feed processor spider.
"""
import scrapy
import csv
from io import StringIO
from ..mixins import SignalAwareSpiderMixin


class CSVFeedSpider(SignalAwareSpiderMixin, scrapy.Spider):
    """
    Spider for processing CSV feeds.
    """
    name = 'csv_feed'
    
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if url:
            self.start_urls = [url]
        else:
            self.start_urls = []
    
    def parse(self, response):
        """
        Parse CSV feed.
        """
        try:
            # Decode response text and parse as CSV
            csv_data = StringIO(response.text)
            reader = csv.DictReader(csv_data)
            
            for row in reader:
                yield {
                    'url': response.url,
                    'row_data': dict(row),
                }
        except Exception as e:
            self.logger.error(f"CSV parsing error: {e}")
            yield {
                'url': response.url,
                'error': str(e),
            }
