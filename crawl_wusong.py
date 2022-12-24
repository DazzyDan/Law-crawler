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


class Crawl_Wusong:
    def __init__(self, search_word, max_page):
        url = "https://www.itslaw.com/home"
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
        self.result = []

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
                    "/html/body/div[1]/div/div[1]/div[2]/div[1]/div[2]/div/div[2]/div[1]/input",
                )
            )
        )
        # 在搜索框输入搜索的关键字
        search_input.send_keys(self.search_word)
        # 回车
        search_input.send_keys(Keys.ENTER)
        self.browser.refresh()
        self.login()
        self.browser.implicitly_wait(15)
        result_dict = self.save_results()
        self.tear_down()
        return result_dict

    def save_results(self):
        # 找到所有的搜索结果
        print("STARTING...")
        # 动态网页 先下一页显示内容 再fetch data
        # next page
        if self.max_page > 1:
            for page in range(1, self.max_page):
                next_page_exist = self.next_page()
                if next_page_exist is False:
                    break

                time.sleep(3)
                # Back to the top
                self.wait.until(
                    EC.element_to_be_clickable((By.CLASS_NAME, "ant-back-top"))
                ).click()

        try:
            results = self.browser.find_elements(
                By.CLASS_NAME, "ListItem__Content-sc-1az4p6x-8"
            )
            for result in results:
                result.find_element(
                    By.CLASS_NAME, "ListItem__TitleStyle-sc-1az4p6x-9"
                ).click()
                newURl = self.browser.window_handles[1]
                self.browser.switch_to.window(newURl)
                # deeper layer with more content in each page by clicking
                content_dict = self.content()
                self.result.append(content_dict)
                self.browser.close()
                self.browser.switch_to.window(self.browser.window_handles[0])
        except exceptions.StaleElementReferenceException as e:
            print("查找标题元素异常")
            print("重新获取元素")
            results = self.browser.find_elements(
                By.CLASS_NAME, "ListItem__Content-sc-1az4p6x-8"
            )
            for result in results:
                result.find_element(
                    By.CLASS_NAME, "ListItem__TitleStyle-sc-1az4p6x-9"
                ).click()
                newURl = self.browser.window_handles[1]
                self.browser.switch_to.window(newURl)
                # deeper layer with more content in each page by clicking
                content_dict = self.content()
                self.result.append(content_dict)
                self.browser.close()
                self.browser.switch_to.window(self.browser.window_handles[0])

        return self.result

    def next_page(self):
        self.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        try:
            if (
                len(
                    self.browser.find_elements(
                        By.CLASS_NAME, "ResultList__LoadMoreStyle-sc-sey7cd-4"
                    )
                )
                > 0
            ):
                # scroll to bottom

                i = self.browser.find_element(
                    By.CLASS_NAME, "ResultList__LoadMoreStyle-sc-sey7cd-4"
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
                        By.CLASS_NAME, "ResultList__LoadMoreStyle-sc-sey7cd-4"
                    )
                )
                > 0
            ):
                # scroll to bottom
                self.browser.execute_script(
                    "window.scrollTo(0, document.body.scrollHeight);"
                )
                i = self.browser.find_element(
                    By.CLASS_NAME, "ResultList__LoadMoreStyle-sc-sey7cd-4"
                )
                self.wait.until(EC.element_to_be_clickable(i)).click()
                return True
            else:
                print("Next page doesn't exist")
                return False

    def login(self):
        # login box will pop out
        # input user name
        user_input = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div[1]/div/div/span/span/input",
                )
            )
        )
        user_input.send_keys("18145132237")
        # input password
        pw_input = self.wait.until(
            EC.presence_of_element_located(
                (
                    By.XPATH,
                    "/html/body/div[4]/div/div[2]/div/div[2]/div[2]/form/div[2]/div/div/span/span/input",
                )
            )
        )
        pw_input.send_keys("EX0w&6t$4A0")
        pw_input.send_keys(Keys.ENTER)

    def content(self):
        content_dict = {}
        title = self.browser.find_element(
            By.CLASS_NAME, "CaseDetail__CaseTitle-sc-6dwb4f-2"
        )
        content_dict["案件标题"] = title.text.strip()
        basic_contents = self.browser.find_elements(
            By.CSS_SELECTOR, ".CaseDetail__DetailText-sc-6dwb4f-11 > dl"
        )

        for basic_content in basic_contents:
            info_name = basic_content.find_element(By.TAG_NAME, "dt").text.strip()
            info_data = basic_content.find_element(By.TAG_NAME, "dd").text.strip()
            content_dict[info_name] = info_data

        more_contents = self.browser.find_elements(
            By.CSS_SELECTOR, ".CaseDetail__SectionContent-sc-6dwb4f-10 > div"
        )
        for more_content in more_contents:
            if "CaseDetail__ParagraphTitle-sc-6dwb4f-13" in str(
                more_content.get_attribute("class")
            ):
                content_dict[more_content.text] = None
            elif "CaseDetail__ParagraphContent-sc-6dwb4f-14" in str(
                more_content.get_attribute("class")
            ):
                answers = more_content.find_elements(By.TAG_NAME, "p")
                final_answer = " ".join([a.text for a in answers])
                content_dict[list(content_dict.keys())[-1]] = final_answer
        return content_dict

    def tear_down(self):
        self.browser.quit()


if __name__ == "__main__":
    import codecs
    import json

    search_word = "诉讼"
    max_page = 1
    search = Crawl_Wusong(search_word, max_page)
    result = search.search()

    with codecs.open("wusong_case.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=4)
