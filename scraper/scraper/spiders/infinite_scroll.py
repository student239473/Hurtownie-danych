import os
import time

import scrapy
from scrapy.selector import Selector
from scrapy_selenium import SeleniumRequest
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class InfiniteScrollSpider(scrapy.Spider):
    name = "infinite_scroll"
    allowed_domains = ["infiniteajaxscroll.com"]
    SCROLL_ROUNDS = 3

    custom_settings = {
        "DOWNLOADER_MIDDLEWARES": {
            "scrapy_selenium.SeleniumMiddleware": 800,
        },
        "SELENIUM_DRIVER_NAME": "chrome",
        "SELENIUM_DRIVER_EXECUTABLE_PATH": os.environ.get("CHROMEDRIVER_PATH"),
        "SELENIUM_DRIVER_ARGUMENTS": ["--headless=new"],
    }

    async def start(self):
        yield SeleniumRequest(
            url="https://infiniteajaxscroll.com/examples/articles/",
            callback=self.parse,
            wait_time=20,
            wait_until=EC.presence_of_element_located(
                (By.CSS_SELECTOR, "h1")
            ),
        )

    def parse(self, response):
        driver = response.meta["driver"]
        driver.implicitly_wait(2)

        for _ in range(self.SCROLL_ROUNDS):
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time.sleep(2)

        selector = Selector(text=driver.page_source)
        yield {
            "url": response.url,
            "content": selector.css(".article").getall(),
        }
