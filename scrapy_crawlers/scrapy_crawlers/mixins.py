"""
Signal-aware spider mixin for connecting to all Scrapy signals.
"""
from scrapy import signals


class SignalAwareSpiderMixin:
    """
    Mixin that connects to all Scrapy signals with stub methods.
    Each spider type can override these methods to implement custom logic.
    """
    
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        """
        Factory method to create spider instance and connect signals.
        """
        spider = super().from_crawler(crawler, *args, **kwargs)
        
        # Connect to all available signals
        crawler.signals.connect(spider.spider_opened, signal=signals.spider_opened)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        crawler.signals.connect(spider.spider_idle, signal=signals.spider_idle)
        crawler.signals.connect(spider.spider_error, signal=signals.spider_error)
        crawler.signals.connect(spider.request_scheduled, signal=signals.request_scheduled)
        crawler.signals.connect(spider.request_dropped, signal=signals.request_dropped)
        crawler.signals.connect(spider.request_reached_downloader, signal=signals.request_reached_downloader)
        crawler.signals.connect(spider.response_received, signal=signals.response_received)
        crawler.signals.connect(spider.response_downloaded, signal=signals.response_downloaded)
        crawler.signals.connect(spider.item_scraped, signal=signals.item_scraped)
        crawler.signals.connect(spider.item_dropped, signal=signals.item_dropped)
        crawler.signals.connect(spider.item_error, signal=signals.item_error)
        
        return spider
    
    def spider_opened(self, spider):
        """Called when spider is opened."""
        pass
    
    def spider_closed(self, spider, reason):
        """Called when spider is closed."""
        pass
    
    def spider_idle(self, spider):
        """Called when spider becomes idle."""
        pass
    
    def spider_error(self, failure, response, spider):
        """Called when spider error occurs."""
        pass
    
    def request_scheduled(self, request, spider):
        """Called when request is scheduled."""
        pass
    
    def request_dropped(self, request, spider):
        """Called when request is dropped."""
        pass
    
    def request_reached_downloader(self, request, spider):
        """Called when request reaches downloader."""
        pass
    
    def response_received(self, response, request, spider):
        """Called when response is received."""
        pass
    
    def response_downloaded(self, response, request, spider):
        """Called when response is downloaded."""
        pass
    
    def item_scraped(self, item, response, spider):
        """Called when item is scraped."""
        pass
    
    def item_dropped(self, item, exception, response, spider):
        """Called when item is dropped."""
        pass
    
    def item_error(self, item, response, spider, failure):
        """Called when item error occurs."""
        pass
