from selenium import webdriver
# from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
import pandas as pd
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path


class Scrape_Baidu:
    def __init__(self, search_word, max_page):
        url = "https://www.baidu.com/"
        self.url = url

        options = webdriver.ChromeOptions()
        options.add_experimental_option(
            "prefs", {"profile.managed_default_content_settings.images": 2}
        )  # 不加载图片,加快访问速度
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"]
        )  # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
        options.add_experimental_option("useAutomationExtension", False)
        self.search_word = search_word
        self.max_page = max_page
        # self.browser = webdriver.Chrome(
        #     ChromeDriverManager().install(), options=options
        # )
        service_object = Service(binary_path)
        self.browser = webdriver.Chrome(service=service_object)
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 10)  # 超时时长为10s
        self.result = {}

    def search(self):
        # 打开百度网页
        self.browser.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {
                "source": 'Object.defineProperty(navigator,"webdriver",{get:()=>undefind})'
            },
        )
        self.browser.get(self.url)
        # 等待搜索框出现，最多等待10秒，否则报超时错误
        search_input = self.wait.until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="kw"]'))
        )
        # 在搜索框输入搜索的关键字
        search_input.send_keys(self.search_word)
        # 回车
        search_input.send_keys(Keys.ENTER)
        # 等待10秒钟
        self.browser.implicitly_wait(10)

        result_dict = self.save_results()
        self.tear_down()
        return result_dict

    def save_results(self):
        # 找到所有的搜索结果
        s = 0
        while True:
            s += 1
            try:
                results = self.browser.find_elements(
                    By.CSS_SELECTOR, ".t a, .c-title-text"
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
                    By.CSS_SELECTOR, ".t a, .c-title-text"
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
            print(f"Scraping {s}/{self.max_page}...")
            if next_page_exist is False or int(s) == int(self.max_page):
                break
        return self.result

    def next_page(self):
        try:
            if len(self.browser.find_elements(By.CSS_SELECTOR, "a.n")) > 0:
                for i in self.browser.find_elements(By.CSS_SELECTOR, "a.n"):
                    if str(i.get_attribute("href")).split("&rsv_page=")[1] == "1":
                        self.wait.until(EC.element_to_be_clickable(i)).click()
                return True
            else:
                print("Next page doesn't exist")
                return False
        except exceptions.StaleElementReferenceException as e:
            print("查找下一页按键元素异常")
            print("重新获取元素")
            if len(self.browser.find_elements(By.CSS_SELECTOR, "a.n")) > 0:
                for i in self.browser.find_elements(By.CSS_SELECTOR, "a.n"):
                    if str(i.get_attribute("href")).split("&rsv_page=")[1] == "1":
                        self.wait.until(EC.element_to_be_clickable(i)).click()
                return True
            else:
                return False

    def tear_down(self):
        try:
            self.browser.quit()
        except exceptions.InvalidSessionIdException as e:
            print(e)


if __name__ == "__main__":
    search_word = "selenium + 案例分析"
    max_page = 2
    search = Scrape_Baidu(search_word, max_page)
    df_baidu = search.search()
    print(df_baidu)
