import re

import scrapy


class HackerNewsSpider(scrapy.Spider):
    name = "hacker_news"
    allowed_domains = ["news.ycombinator.com"]
    start_urls = ["https://news.ycombinator.com/news"]

    custom_settings = {
        "CONCURRENT_REQUESTS_PER_DOMAIN": 1,
        "DOWNLOAD_DELAY": 30,
    }

    def __init__(self, pages="1", **kwargs):
        super().__init__(**kwargs)
        try:
            self.pages = int(pages)
        except ValueError as exc:
            raise ValueError("pages must be a positive integer") from exc
        if self.pages < 1:
            raise ValueError("pages must be a positive integer")

    def parse(self, response):
        page = response.meta.get("page", 1)
        for story in response.css("tr.athing"):
            title_link = story.css("span.titleline > a")
            title = title_link.css("::text").get()
            if not title:
                continue

            subtext = story.xpath(
                "following-sibling::tr[1]//td[contains(@class, 'subtext')]"
            )
            comment_label = next(
                (
                    text.strip()
                    for text in subtext.xpath(".//a/text()").getall()
                    if "comment" in text.lower() or text.strip().lower() == "discuss"
                ),
                None,
            )
            comment_count = (
                int(re.search(r"\d+", comment_label).group())
                if comment_label and re.search(r"\d+", comment_label)
                else 0
            )
            score = subtext.css("span.score::text").re_first(r"\d+")
            yield {
                "source": "hacker_news",
                "story_id": story.attrib.get("id"),
                "title": title.strip(),
                "url": title_link.attrib.get("href"),
                "score": int(score) if score else 0,
                "author": subtext.css("a.hnuser::text").get(),
                "published_at": subtext.css("span.age::attr(title)").get(),
                "comments": comment_count,
            }

        next_page = response.css("a.morelink::attr(href)").get()
        if next_page and page < self.pages:
            yield response.follow(
                next_page,
                callback=self.parse,
                meta={"page": page + 1},
            )
