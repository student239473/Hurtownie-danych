import scrapy

from scraper.spiders import RSSNewsSpider


class NYTWorldNewsSpider(RSSNewsSpider, scrapy.Spider):
    name = "nyt_world_news"
    source_name = "nyt_world_news"
    allowed_domains = ["rss.nytimes.com"]
    start_urls = ["https://rss.nytimes.com/services/xml/rss/nyt/World.xml"]
