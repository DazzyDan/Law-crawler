from flask import Flask
from law_crawler.blueprint.home import home
from law_crawler.blueprint.search_case import casesearch
from law_crawler.blueprint.search_web import websearch


class LawCrawlerApp(Flask):
    def __init__(self) -> None:
        super().__init__(__name__, static_url_path="/static")
        self._init_register()

    def _init_register(self):
        self.register_blueprint(home)
        self.register_blueprint(casesearch)
        self.register_blueprint(websearch)
