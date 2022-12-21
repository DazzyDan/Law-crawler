from flask import Flask, render_template, request
from scrape_baidu import Scrape_Baidu
from scrape_sogou import Scrape_Sogou
from scrape_wechat import Scrape_Wechat
import time

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    return "Hello World"


@app.route("/search-wd", methods=["GET", "POST"])
def search_wd():
    dict_concat = {}
    baidu_dict = {}
    sogou_dict = {}
    wechat_dict = {}
    if request.method == "POST":
        search_wd = request.form["search_wd_input"]
        search_page = request.form["search_page"]
        search_method = request.form.getlist("search_method")
        error = None
        print(search_wd)
        print(search_page)
        if not search_wd:
            error = "search_wd is required."
        elif not search_page:
            error = "search_page is required."
        elif not search_method:
            error = "search_method is required"

        if error is None:
            for i in search_method:
                if i == "baidu":
                    baidu = Scrape_Baidu(search_wd, search_page)
                    baidu_dict = baidu.search()
                    time.sleep(1)
                elif i == "sogou":
                    sogou = Scrape_Sogou(search_wd, search_page)
                    sogou_dict = sogou.search()
                    time.sleep(1)
                elif i == "wechat":
                    wechat = Scrape_Wechat(search_wd, search_page)
                    wechat_dict = wechat.search()
            dict_concat = {**baidu_dict, **sogou_dict, **wechat_dict}
    return render_template("homepage.html", results=dict_concat)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
