from __future__ import annotations

from law_crawler.scraper.scraper_getter.scraper_getter import ScrapeGetter
from law_crawler.scraper.scraped_dataclass import SearchEngineScrapedData

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class WechatScrapeGetter:
    def __init__(self) -> None:
        super().__init__()
        self.url = "https://weixin.sogou.com/"
        self.browser = webdriver.Chrome("chromedriver_mac64/chromedriver")
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 10)  # 超时时长为10s
        self.result = {}

    def get(self, key_word: str, page_nbr: int) -> list[SearchEngineScrapedData]:
        # 打开百度网页
        self.browser.get(self.url)
        # 等待搜索框出现，最多等待10秒，否则报超时错误
        search_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="query"]'))
        )
        # 在搜索框输入搜索的关键字
        search_input.send_keys(key_word)
        # 回车
        search_input.send_keys(Keys.ENTER)
        # 等待10秒钟
        self.browser.implicitly_wait(10)

        result_dict = self.save_results(page_nbr)
        self.tear_down()

        return [
            SearchEngineScrapedData(link=link, title=title)
            for link, title in result_dict.items()
        ]

    def save_results(self, page_nbr):
        # 找到所有的搜索结果
        s = 0
        while True:
            s += 1
            try:
                results = self.browser.find_elements(
                    By.CSS_SELECTOR, ".txt-box > h3 > a"
                )
                for result in results:
                    if result.get_attribute("href"):
                        # 搜索结果的标题
                        title = result.text.strip()
                        # 搜索结果的网址
                        link = result.get_attribute("href")
                        if link not in self.result.keys():
                            self.result[link] = title
            except exceptions.StaleElementReferenceException as e:
                print("查找元素异常")
                print("重新获取元素")
                results = self.browser.find_elements(
                    By.CSS_SELECTOR, ".txt-box > h3 > a"
                )
                for result in results:
                    if result.get_attribute("href"):
                        # 搜索结果的标题
                        title = result.text.strip()
                        # 搜索结果的网址
                        link = result.get_attribute("href")
                        if link not in self.result.keys():
                            self.result[link] = title

            next_page_exist = self.next_page()
            print(f"Scraping {s}/{page_nbr}...")
            if next_page_exist is False or int(s) == int(page_nbr):
                break
        return self.result

    def next_page(self):
        try:
            if len(self.browser.find_elements(By.ID, "sogou_next")) > 0:
                i = self.browser.find_element(By.ID, "sogou_next")
                self.wait.until(EC.element_to_be_clickable(i)).click()
                return True
            else:
                print("Next page doesn't exist")
                return False
        except exceptions.StaleElementReferenceException as e:
            print("查找下一页按键元素异常")
            print("重新获取元素")
            if len(self.browser.find_elements(By.ID, "sogou_next")) > 0:
                i = self.browser.find_element(By.ID, "sogou_next")
                self.wait.until(EC.element_to_be_clickable(i)).click()
                return True
            else:
                return False

    def tear_down(self):
        try:
            self.browser.quit()
        except exceptions.InvalidSessionIdException as e:
            print(e)
