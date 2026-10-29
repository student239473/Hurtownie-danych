import scrapy

from scraper.spiders import RSSNewsSpider


class SkyNewsSpider(RSSNewsSpider, scrapy.Spider):
    name = "sky_news"
    source_name = "sky_news"
    allowed_domains = ["feeds.skynews.com"]
    start_urls = ["https://feeds.skynews.com/feeds/rss/world.xml"]
