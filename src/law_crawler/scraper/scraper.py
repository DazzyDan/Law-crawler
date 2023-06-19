from law_crawler.scraper.scraped_dataclass import (
    SearchEngineScrapedData,
    LawWebScrapedData,
)


class Scraper:
    @classmethod
    def get(cls, key_word, page_nbr, getter):
        # FIXME: how can it remove parenthesis
        return getter().get(key_word, page_nbr)

    @classmethod
    def get_search_engine_result(cls, key_word, page_nbr, getter):
        res_list = cls.get(key_word, page_nbr, getter)
        return [SearchEngineScrapedData(res.link, res.title) for res in res_list]

    @classmethod
    def get_law_web_result(cls, key_word, page_nbr, getter):
        res_list = cls.get(key_word, page_nbr, getter)
        return [LawWebScrapedData(res) for res in res_list]


if __name__ == "__main__":
    from law_crawler.scraper.scraper_getter.search_engine_scraper_getter import (
        BaiduScrapeGetter,
    )

    result = Scraper.get_search_engine_result("陆冲价格", 1, BaiduScrapeGetter)
    print(result)
