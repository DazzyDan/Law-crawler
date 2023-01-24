from flask import Flask, render_template, request
from scrape.baidu import Scrape_Baidu
from scrape.sogou import Scrape_Sogou
from scrape.wechat import Scrape_Wechat
from scrape.bashou import Scrape_Bashou
from scrape.wusong import Scrape_Wusong
import time

# import json, codecs

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return render_template("homepage.html")


@app.route("/search-web", methods=["GET", "POST"])
def search_wd():
    dict_concat = {}
    baidu_dict = {}
    sogou_dict = {}
    wechat_dict = {}
    if request.method == "POST":
        search_wd = request.form["search_wd_input"]
        search_page = request.form["search_page"]
        search_method = request.form.getlist("case_chose")
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
    return render_template("search_web.html", results=dict_concat)


@app.route("/search-case", methods=["GET", "POST"])
def search_case():
    list_concat = []
    bashou_list = []
    wusong_list = []
    if request.method == "POST":
        search_wd = request.form["search_wd_input"]
        search_page = request.form["search_page"]
        case_type = request.form.getlist("case_chose")
        error = None
        # print(search_wd)
        # print(search_page)
        # print(case_type)
        if not search_wd:
            error = "search wd is required."
        elif not search_page:
            error = "search page is required."
        elif not case_type:
            error = "case type is required"

        if error is None:
            # bashou
            for type in case_type:
                bashou = Scrape_Bashou(search_wd, search_page, type)
                bashou_list = bashou.search()
                time.sleep(3)
            # wusong
            wusong = Scrape_Wusong(search_wd, search_page)
            wusong_list = wusong.search()
            list_concat = bashou_list + wusong_list

    return render_template("search_case.html", results=list_concat)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
