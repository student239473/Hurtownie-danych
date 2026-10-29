# Infinite-scroll demo spider

The `infinite_scroll` spider demonstrates Selenium scrolling on the public
Scrapy practice page `https://infiniteajaxscroll.com/examples/articles/`.
It is separate from the news spiders and the PAP spider.

Install the project dependencies from the repository root:

```powershell
uv sync
```

Install ChromeDriver that matches your Chrome browser, then set
`CHROMEDRIVER_PATH` to the full path of `chromedriver.exe` in PowerShell:

```powershell
$env:CHROMEDRIVER_PATH = "C:\path\to\chromedriver.exe"
```

Run the spider from the `scraper` directory:

```powershell
uv run --project .. scrapy crawl infinite_scroll -O ..\infinite_scroll.jsonl
```

## News spiders

The project includes ten independent news spiders:

| Spider | Source | Data |
| --- | --- | --- |
| `hacker_news` | [Hacker News](https://news.ycombinator.com/) | Front-page story titles, links, scores, authors, timestamps, and comment counts |
| `bbc_news_rss` | [BBC News RSS](https://feeds.bbci.co.uk/news/rss.xml) | Feed titles, summaries, links, publication dates, and thumbnails |
| `npr_news` | [NPR News RSS](https://feeds.npr.org/1001/rss.xml) | News feed entries |
| `dw_news` | [DW News RSS](https://rss.dw.com/rdf/rss-en-all) | News feed entries |
| `al_jazeera_news` | [Al Jazeera RSS](https://www.aljazeera.com/xml/rss/all.xml) | News feed entries |
| `france24_news` | [France 24 RSS](https://www.france24.com/en/rss) | News feed entries |
| `euronews` | [Euronews RSS](https://www.euronews.com/rss?level=theme&name=news) | News feed entries |
| `sky_news` | [Sky News RSS](https://feeds.skynews.com/feeds/rss/world.xml) | World news feed entries |
| `nyt_world_news` | [New York Times World RSS](https://rss.nytimes.com/services/xml/rss/nyt/World.xml) | World news feed entries |
| `pbs_news` | [PBS NewsHour RSS](https://www.pbs.org/newshour/feeds/rss/headlines) | News feed entries |

Run these commands from the `scraper` directory. They write JSON Lines output
files into the repository root:

```powershell
uv run --project .. scrapy crawl hacker_news -O ..\hacker_news.jsonl
uv run --project .. scrapy crawl bbc_news_rss -O ..\bbc_news.jsonl
uv run --project .. scrapy crawl npr_news -O ..\npr_news.jsonl
uv run --project .. scrapy crawl dw_news -O ..\dw_news.jsonl
uv run --project .. scrapy crawl al_jazeera_news -O ..\al_jazeera_news.jsonl
uv run --project .. scrapy crawl france24_news -O ..\france24_news.jsonl
uv run --project .. scrapy crawl euronews -O ..\euronews.jsonl
uv run --project .. scrapy crawl sky_news -O ..\sky_news.jsonl
uv run --project .. scrapy crawl nyt_world_news -O ..\nyt_world_news.jsonl
uv run --project .. scrapy crawl pbs_news -O ..\pbs_news.jsonl
```

Hacker News has a 30-second crawl delay in its `robots.txt`; the spider uses
that delay and reads one front-page listing by default. To read more listing
pages, pass a positive page count with `-a pages=2`.

The BBC spider reads the RSS feed rather than crawling article pages. Follow
the BBC's [RSS reuse terms](https://www.bbc.co.uk/usingthebbc/terms-of-use/#15metadataandrssfeeds)
when using the results.

The eight additional news spiders read public RSS/XML feeds (including DW's
RSS 1.0/RDF feed); they do not call the Guardian API or crawl article pages.
Respect each publisher's feed terms when storing or reusing its content.
