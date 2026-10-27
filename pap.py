import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PapSpider(CrawlSpider):
    name = "pap"
    allowed_domains = ["pap.pl"]
    start_urls = ["https://pap.pl"]

    rules = Rule(
        LinkExtractor(allow=(r"/aktualnosci/[^/?#]+/?$",)),
        callback="parse_item",
        follow=False,
    ),
    def parse_item(self, response):
        return {
            "url": response.url,
            "title": response.css("h1::text").get(),
            "text": " ".join(
                response.css(".field--name-body ::text").getall()
            ).strip(),
        }
