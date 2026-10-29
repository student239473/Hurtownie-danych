import scrapy

from scraper.spiders import RSSNewsSpider


class BBCNewsRSSSpider(RSSNewsSpider, scrapy.Spider):
    name = "bbc_news_rss"
    source_name = "bbc_news"
    allowed_domains = ["feeds.bbci.co.uk"]
    start_urls = ["https://feeds.bbci.co.uk/news/rss.xml"]
