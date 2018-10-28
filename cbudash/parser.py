#!/usr/bin(/env python3

import datetime

from bs4 import BeautifulSoup

from cbudash.data import NewsGroup, NewsItem

TR_MONTHS = {
    'Oca': 1,
    'Şub': 2,
    'Mar': 3,
    'Nis': 4,
    'May': 5,
    'Haz': 6,
    'Tem': 7,
    'Ağu': 8,
    'Eyl': 9,
    'Eki': 10,
    'Kas': 11,
    'Ara': 12
}


class BaseParser:
    def __init__(self):
        self.name = 'BaseParser'

    def parse(self, html: str, limit: int = -1) -> NewsGroup:
        raise NotImplementedError


class CBUParser(BaseParser):

    def __init__(self):
        super().__init__()

        self.name = 'CBUParser'

    def parse(self, html: str, limit: int = -1, as_dict=False) -> NewsGroup:
        result = NewsGroup()

        soup = BeautifulSoup(html, 'html.parser')
        links = soup.find_all(attrs={'class': 'CustomNewsLink'})

        for link in links:
            url = link['href']

            link_header = link.find(attrs={'class': 'CustomLiHeader'}).text
            link_title = link.find(attrs={'class': 'CustomLiP'}).text

            link_header = link_header.split('::')

            date = self._parse_date(link_header[0].strip())
            category = link_header[-1].strip()
            title = link_title.strip()

            result.append(NewsItem(date, category, title, url))

            if len(result) >= limit > 0:
                break

        return result if not as_dict else result.to_dict()

    def _parse_date(self, date_str) -> datetime.date:
        tokens = date_str.split('.')

        day = int(tokens[0].strip())
        month = TR_MONTHS[tokens[1].strip()]
        year = int(tokens[2].strip()) + 2000

        return datetime.date(year=year, month=month, day=day)
