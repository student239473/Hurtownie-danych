import scrapy

from scraper.spiders import RSSNewsSpider


class DWNewsSpider(RSSNewsSpider, scrapy.Spider):
    name = "dw_news"
    source_name = "dw_news"
    allowed_domains = ["rss.dw.com"]
    start_urls = ["https://rss.dw.com/rdf/rss-en-all"]
