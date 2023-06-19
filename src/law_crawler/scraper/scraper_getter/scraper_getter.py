from __future__ import annotations
from abc import ABC, abstractclassmethod
from law_crawler.scraper.scraped_dataclass import (
    SearchEngineScrapedData,
    LawWebScrapedData,
)


class ScrapeGetter(ABC):
    @abstractclassmethod
    def get(
        self, key_word: str, page_nbr: int
    ) -> list[SearchEngineScrapedData] | list[LawWebScrapedData]:
        ...
