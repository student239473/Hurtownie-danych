import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class PapSpider(CrawlSpider):
    name = "pap"
    allowed_domains = ["pap.pl"]
    start_urls = ["https://www.pap.pl/aktualnosci/w-czwartek-tansza-benzyna-95-i-diesel-drozsza-benzyna-98"]

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
