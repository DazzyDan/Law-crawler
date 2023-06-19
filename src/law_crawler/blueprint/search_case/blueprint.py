import flask
import time

from law_crawler.scraper.bashou import Scrape_Bashou
from law_crawler.scraper.wusong import Scrape_Wusong


casesearch = flask.Blueprint(
    "casesearch", import_name=__name__, template_folder="templates"
)


@casesearch.route("/search-case", methods=["GET", "POST"])
def search_case():
    list_concat = []
    bashou_list = []
    wusong_list = []
    if flask.request.method == "POST":
        search_wd = flask.request.form["search_wd_input"]
        search_page = flask.request.form["search_page"]
        case_type = flask.request.form.getlist("case_chose")
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

    return flask.render_template("search_case.html", results=list_concat)
