from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
import time


class Crawl_Bashou:
    def __init__(self, search_word, max_page, case_type):
        url = "https://www.lawsdata.com/#/home"
        self.url = url

        options = webdriver.ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--no-sandbox")
        options.add_experimental_option(
            "prefs", {"profile.managed_default_content_settings.images": 2}
        )  # 不加载图片,加快访问速度
        options.add_experimental_option(
            "excludeSwitches", ["enable-automation"]
        )  # 此步骤很重要，设置为开发者模式，防止被各大网站识别出来使用了Selenium
        options.add_experimental_option("useAutomationExtension", False)
        service_object = Service(binary_path)
        self.browser = webdriver.Chrome(service=service_object)
        self.browser.maximize_window()
        self.wait = WebDriverWait(self.browser, 10)  # 超时时长为10s
        self.search_word = search_word
        self.max_page = max_page
        self.case_type = case_type
        self.result = {}
        # self.browser = webdriver.Chrome(
        #     ChromeDriverManager().install(), options=options
        # )

    def search(self):
        self.browser.execute_cdp_cmd(
            "Page.addScriptToEvaluateOnNewDocument",
            {
                "source": 'Object.defineProperty(navigator,"webdriver",{get:()=>undefind})'
            },
        )
        self.browser.get(self.url)

        # 等待搜索框出现，最多等待10秒，否则报超时错误
        search_input = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div[3]/div/div/div[1]/div[3]/div/div[1]/div[2]/input",
                )
            )
        )
        # 在搜索框输入搜索的关键字
        search_input.send_keys(self.search_word)
        # 回车
        search_input.send_keys(Keys.ENTER)
        # 等待10秒钟
        self.browser.implicitly_wait(10)
        self.login()
        self.select_case_type()
        result_dict = self.save_results()

        self.tear_down()
        # return result_dict

    def select_case_type(self):
        #'高院案例', '权威案例', '普通案例'
        case_types = self.browser.find_elements(
            By.CSS_SELECTOR, ".list-top > .left > ul > li"
        )
        for case_type in case_types:
            if self.case_type == case_type.text.split("(")[0].strip():
                print(case_type.text.split("(")[0].strip(), ":", self.case_type)
                self.wait.until(EC.element_to_be_clickable(case_type)).click()

    def save_results(self):
        # 找到所有的搜索结果
        s = 0
        while True:
            print("STARTING...")
            s += 1
            results = self.browser.find_elements(
                By.CSS_SELECTOR, "#resultList > .right > .result-list"
            )[1].find_elements(By.CSS_SELECTOR, ".box")
            for result in results:
                title = result.find_element(By.CSS_SELECTOR, ".title > p").text.strip()
                ref_type = result.find_element(
                    By.CSS_SELECTOR, ".title > .right-title> .right-span"
                ).text
                case_footers = result.find_elements(
                    By.CSS_SELECTOR, ".cont > .case-footer > ul > li"
                )
                court = case_footers[0].text
                cause_of_action = case_footers[1].text
                trial_procedure = case_footers[2].text
                doc_type = case_footers[3].text
                case_num = case_footers[4].text

                # deeper layer with more content in each page by clicking
                self.content(result)

            next_page_exist = self.next_page()
            print(f"Scraping {s}/{self.max_page}...")
            if next_page_exist is False or int(s) == int(self.max_page):
                break

        return self.result

    def next_page(self):
        try:
            ## browser should be maximized otherwise another element overlaps the 'next page' button
            if (
                len(
                    self.browser.find_elements(
                        By.CSS_SELECTOR, ".page > ul > .ant-pagination-next"
                    )
                )
                > 0
            ):
                i = self.browser.find_element(
                    By.CSS_SELECTOR, ".page > ul > .ant-pagination-next"
                )
                self.wait.until(EC.element_to_be_clickable(i)).click()
                return True
            else:
                print("Next page doesn't exist")
                return False
        except exceptions.StaleElementReferenceException as e:
            print("查找下一页按键元素异常")
            print("重新获取元素")
            if (
                len(
                    self.browser.find_elements(
                        By.CSS_SELECTOR, ".page > ul > .ant-pagination-next"
                    )
                )
                > 0
            ):
                i = self.browser.find_element(
                    By.CSS_SELECTOR, ".page > ul > .ant-pagination-next"
                )
                self.wait.until(EC.element_to_be_clickable(i)).click()
                return True
            else:
                print("Next page doesn't exist")
                return False

    def login(self):
        # login box
        self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    '//*[@id="app"]/div[3]/div/div/div/div/div[1]/div[1]/div/div[2]/button',
                )
            )
        ).click()

        # input user name
        user_input = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div[7]/div/form/div[1]/div/div/span/input",
                )
            )
        )
        user_input.send_keys("18145132237")
        # input password
        pw_input = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[1]/div[7]/div/form/div[2]/div/div/span/input",
                )
            )
        )
        pw_input.send_keys("bYK3B27i3jtF6")

        # login button
        login_btn = self.browser.find_element(
            By.XPATH, "/html/body/div[1]/div[7]/div/form/div[4]/div/div/span/button"
        )

        login_btn.click()

    def content(self, result):
        result.find_element(By.CSS_SELECTOR, ".title > p").click()
        newURl = self.browser.window_handles[1]
        self.browser.switch_to.window(newURl)
        contents = self.browser.find_elements(By.CLASS_NAME, "caipanBody")
        for content in contents:
            name = content.find_element(
                By.CSS_SELECTOR, ".caipanyaodian > .typeText"
            ).text
            answers = content.find_elements(By.CLASS_NAME, "yaodianMsg")
            final_answer = " ".join([a.text for a in answers])
            print(name, " : ", final_answer)

        ## Solution: output all the info and use 'if' or 'dict' to fetch it later
        # 争议焦点
        # 诉讼请求
        # 裁判结果 id= type6 / type8
        # 法律依据 相关法条 id = type2
        # 审结日期
        self.browser.close()
        self.browser.switch_to.window(self.browser.window_handles[0])

    def tear_down(self):
        self.browser.quit()


if __name__ == "__main__":
    search_word = "诉讼"
    max_page = 2
    case_type = "高院案例"
    search = Crawl_Bashou(search_word, max_page, case_type)
    search.search()
