from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common import exceptions
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from chromedriver_py import binary_path
from selenium.common.exceptions import NoSuchElementException
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
        self.wait = WebDriverWait(self.browser, 20)  # 超时时长为10s
        self.search_word = search_word
        self.max_page = max_page
        self.case_type = case_type
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
        case_result = self.save_results()

        self.tear_down()
        return case_result

    def select_case_type(self):
        #'高院案例', '权威案例', '普通案例'
        case_types = self.browser.find_elements(
            By.CSS_SELECTOR,
            "#resultList>.right>.result-list>.list-top > .left > ul > li",
        )
        for case_type in case_types:
            if self.case_type == case_type.text.split("(")[0].strip():
                # print(case_type.text.split("(")[0].strip(), ":", self.case_type)
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
                # deeper layer with more content in each page by clicking
                # To the deeper page
                result.find_element(By.CSS_SELECTOR, ".title > p").click()
                newURl = self.browser.window_handles[1]
                self.browser.switch_to.window(newURl)
                # Skip intro
                try:
                    self.browser.find_element(
                        By.CLASS_NAME, "introjs-skipbutton"
                    ).click()
                except NoSuchElementException:
                    print("Not found skip button...")

                # Fetch useful data
                case = self.content()
                self.result.append(case)
                print(self.result)
                # Back to the original page
                self.browser.close()
                self.browser.switch_to.window(self.browser.window_handles[0])

            next_page_exist = self.next_page()
            print(f"Scraping {s}/{self.max_page}...")
            if next_page_exist is False or int(s) == int(self.max_page):
                break
            print(self.result)
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
            EC.element_to_be_clickable(
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

    def content(self):
        case = {}
        # Fetch useful data
        time.sleep(3)
        # 案由
        title = self.browser.find_element(By.CLASS_NAME, "titleBiao").text.strip()
        case["案由"] = title
        # 基本信息
        basic_info = self.browser.find_elements(By.CLASS_NAME, "jibenLi")
        for i in basic_info:
            info_name = "".join(
                [
                    t.text.strip()
                    for t in i.find_elements(By.CSS_SELECTOR, ".jibendivone > span")
                ]
            )
            print(info_name)
            if info_name == "案例来源":
                info_value = i.find_element(By.CLASS_NAME, "jibendivtwo1").text.strip()
                continue
            elif info_name == "案号":
                # 案号 需要点击显示全部案号
                case_num_eye = i.find_element(
                    By.CSS_SELECTOR, ".jibendivtwo > div > img"
                )
                self.wait.until(EC.element_to_be_clickable(case_num_eye)).click()
            info_value = i.find_element(By.CLASS_NAME, "jibendivtwo").text.strip()
            print(info_value)
            case[info_name] = info_value
        # 侧边信息
        try:
            other_info = self.browser.find_elements(By.CLASS_NAME, "fatiaofagui")
            for i in other_info:
                info_key = i.find_element(By.CLASS_NAME, "jibenxinxibiaoti")
                if "法律依据" in info_key:
                    legals = i.find_elements(
                        By.CSS_SELECTOR, ".ant-collapse-header > div:nth-child(2)"
                    )
                    legal_basis = [l.text.split("查")[0].strip() for l in legals]
                    case["法律依据"] = legal_basis
                    print(legal_basis)
                elif "诉讼请求" in info_key:
                    lawsuit_req = i.find_element(
                        By.CLASS_NAME, "fatiaofaguiOver"
                    ).text.strip()
                    case["诉讼请求"] = lawsuit_req
                    print(lawsuit_req)
        except NoSuchElementException:
            print("Not found other info like legals or lawsuit...")

        # 案情细节
        contents = self.browser.find_elements(By.CLASS_NAME, "caipanBody")
        for content in contents:
            cont_name = content.find_element(
                By.CSS_SELECTOR, ".caipanyaodian > .typeText"
            ).text.strip()
            cont_value = content.find_elements(By.CLASS_NAME, "yaodianMsg")
            final_cont_value = " ".join([a.text for a in cont_value])

            case[cont_name] = final_cont_value
        return case

    def tear_down(self):
        self.browser.quit()


if __name__ == "__main__":
    import json

    search_word = "诉讼"
    max_page = 1
    case_type = "普通案例"
    search = Crawl_Bashou(search_word, max_page, case_type)
    case_result = search.search()
    with open("bashou_case.json", "w") as fp:
        json.dump(case_result, fp, indent=4)
