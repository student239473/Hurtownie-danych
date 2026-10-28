# Infinite-scroll demo spider

The `infinite_scroll` spider demonstrates Selenium scrolling on the public
Scrapy practice page `https://infiniteajaxscroll.com/examples/articles/`.
It is separate from the PAP spider.

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
