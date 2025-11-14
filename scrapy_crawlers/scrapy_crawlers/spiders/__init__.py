# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from .basic_spider import BasicSpider
from .crawl_link_spider import CrawlLinkSpider
from .sitemap_crawler_spider import SitemapCrawlerSpider
from .api_harvester_spider import APIHarvesterSpider
from .rss_feed_spider import RSSFeedSpider
from .csv_feed_spider import CSVFeedSpider
from .json_feed_spider import JSONFeedSpider
from .link_extractor_spider import LinkExtractorSpider
from .archival_spider import ArchivalSpider
from .darknet_spider import DarknetSpider
from .custom_spider import CustomSpider

__all__ = [
    'BasicSpider',
    'CrawlLinkSpider',
    'SitemapCrawlerSpider',
    'APIHarvesterSpider',
    'RSSFeedSpider',
    'CSVFeedSpider',
    'JSONFeedSpider',
    'LinkExtractorSpider',
    'ArchivalSpider',
    'DarknetSpider',
    'CustomSpider',
]
