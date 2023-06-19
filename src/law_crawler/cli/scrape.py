import argparse
import sys
from law_crawler.scraper.scraper import Scraper
from law_crawler.scraper.scraper_getter.search_engine_scraper_getter import (
    BaiduScrapeGetter,
    SogouScrapeGetter,
    WechatScrapeGetter,
)


def main(argv=sys.argv[1:]):
    parser = argparse.ArgumentParser(description="Scrape CLI")
    # FIXME: Add required=True,
    parser.add_argument("--source", "-s", help="Souce name to be scraped")
    parser.add_argument("--keyword", "-kw", help="Key words to be searched")
    parser.add_argument("--page", "-p", default=1, help="The nbr of scraping pages")

    args = parser.parse_args(argv)
    source = str(args.source)
    keyword = str(args.keyword)
    page = int(args.page)
    print(page)
    # FIXME: run multiple sources
    if source.lower().strip() == "baidu":
        getter = BaiduScrapeGetter
    elif source.lower().strip() == "sogou":
        getter = SogouScrapeGetter
    elif source.lower().strip() == "wechat":
        getter = WechatScrapeGetter
    return Scraper.get_search_engine_result(
        key_word=keyword, page_nbr=page, getter=getter
    )


if __name__ == "__main__":
    result = main()
    print(result)
