import scrapy

from scraper.spiders import RSSNewsSpider


class PBSNewsSpider(RSSNewsSpider, scrapy.Spider):
    name = "pbs_news"
    source_name = "pbs_news"
    allowed_domains = ["www.pbs.org"]
    start_urls = ["https://www.pbs.org/newshour/feeds/rss/headlines"]
