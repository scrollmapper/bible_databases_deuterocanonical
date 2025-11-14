"""
Sitemap crawler spider.
"""
from scrapy.spiders import SitemapSpider
from ..mixins import SignalAwareSpiderMixin


class SitemapCrawlerSpider(SignalAwareSpiderMixin, SitemapSpider):
    """
    Spider that crawls URLs from a sitemap.
    """
    name = 'sitemap'
    
    def __init__(self, url=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if url:
            # Assume the URL is the sitemap URL
            self.sitemap_urls = [url]
        else:
            self.sitemap_urls = []
    
    def parse(self, response):
        """
        Parse each URL from sitemap.
        """
        yield {
            'url': response.url,
            'status': response.status,
            'title': response.css('title::text').get(),
        }
