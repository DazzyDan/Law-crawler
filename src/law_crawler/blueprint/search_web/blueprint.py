import flask
import time

from law_crawler.scraper.baidu import Scrape_Baidu
from law_crawler.scraper.sogou import Scrape_Sogou
from law_crawler.scraper.wechat import Scrape_Wechat

websearch = flask.Blueprint(
    "websearch", import_name=__name__, template_folder="templates"
)


@websearch.route("/search-web", methods=["GET", "POST"])
def search_wd():
    dict_concat = {}
    baidu_dict = {}
    sogou_dict = {}
    wechat_dict = {}
    if flask.request.method == "POST":
        search_wd = flask.request.form["search_wd_input"]
        search_page = flask.request.form["search_page"]
        search_method = flask.request.form.getlist("case_chose")
        error = None
        print(search_wd)
        print(search_page)
        print(search_method)
        if not search_wd:
            error = "search_wd is required."
        elif not search_page:
            error = "search_page is required."
        elif not search_method:
            error = "search_method is required"

        if error is None:
            if "百度" in search_method:
                # with codecs.open("baidu_case.json", "r", "utf-8") as data_file:
                #     baidu_dict = json.load(data_file)
                baidu = Scrape_Baidu(search_wd, search_page)
                baidu_dict = baidu.search()
                time.sleep(1)
            if "搜狗" in search_method:
                # with codecs.open("sogou_case.json", "r", "utf-8") as data_file:
                #     sogou_dict = json.load(data_file)
                sogou = Scrape_Sogou(search_wd, search_page)
                sogou_dict = sogou.search()
                time.sleep(1)
            if "微信" in search_method:
                # with codecs.open("wechat_case.json", "r", "utf-8") as data_file:
                #     wechat_dict = json.load(data_file)
                wechat = Scrape_Wechat(search_wd, search_page)
                wechat_dict = wechat.search()
            dict_concat = {**baidu_dict, **sogou_dict, **wechat_dict}
    return flask.render_template("search_web.html", results=dict_concat)
