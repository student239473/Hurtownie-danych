class RSSNewsSpider:
    source_name = ""

    def parse(self, response):
        for entry in response.xpath(
            "//*[local-name()='item' or local-name()='entry']"
        ):
            title = entry.xpath("string(./*[local-name()='title'])").get()
            if not title:
                continue

            link = entry.xpath("string(./*[local-name()='link'])").get()
            if not link:
                link = entry.xpath("./*[local-name()='link']/@href").get()
            if not link:
                link = entry.xpath("./@*[local-name()='about']").get()

            summary = next(
                (
                    value
                    for field in ("description", "summary", "encoded")
                    if (
                        value := entry.xpath(
                            f"string(./*[local-name()='{field}'])"
                        ).get()
                    )
                ),
                None,
            )
            published_at = next(
                (
                    value
                    for field in ("pubDate", "published", "updated", "date")
                    if (
                        value := entry.xpath(
                            f"string(./*[local-name()='{field}'])"
                        ).get()
                    )
                ),
                None,
            )
            thumbnail = entry.xpath(
                "./*[local-name()='thumbnail']/@url | "
                "./*[local-name()='content']/@url | "
                "./*[local-name()='enclosure']/@url"
            ).get()

            yield {
                "source": self.source_name,
                "title": title.strip(),
                "url": link.strip() if link else None,
                "summary": summary.strip() if summary else None,
                "published_at": published_at.strip() if published_at else None,
                "thumbnail": thumbnail,
            }
