"""
Dark web crawler spider (Tor-enabled).
"""
import scrapy
from ..mixins import SignalAwareSpiderMixin


class DarknetSpider(SignalAwareSpiderMixin, scrapy.Spider):
    """
    Spider configured for dark web crawling.
    Note: Requires proper Tor configuration in settings.
    """
    name = 'darknet'
    
    # Custom settings for Tor
    custom_settings = {
        'DOWNLOAD_HANDLERS': {
            'http': 'scrapy.core.downloader.handlers.http.HTTPDownloadHandler',
            'https': 'scrapy.core.downloader.handlers.http.HTTPDownloadHandler',
        },
        # Note: In production, configure HTTP_PROXY and HTTPS_PROXY for Tor
        # 'HTTP_PROXY': 'http://127.0.0.1:9050',
        # 'HTTPS_PROXY': 'http://127.0.0.1:9050',
    }
    
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if url:
            self.start_urls = [url]
        else:
            self.start_urls = []
    
    def parse(self, response):
        """
        Parse dark web page.
        """
        yield {
            'url': response.url,
            'status': response.status,
            'title': response.css('title::text').get(),
            'onion_address': '.onion' in response.url,
        }
