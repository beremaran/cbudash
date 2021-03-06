#!/usr/bin/env python3

import json
import requests

from cbudash.parser import BaseParser, CBUParser


class CBUDash:
    def __init__(self, config: str = './config.json'):
        self.config = json.load(open(config, 'r'))
        self.sources = []
        self.parsers = {}

        # register parsers
        self._register_parser(CBUParser())

        # register sources
        for source in self.config['sources']:
            self._register_source(source)

    def get(self, as_dict=False) -> list:
        return self._parse_sources(as_dict)

    def _register_parser(self, parser: BaseParser):
        self.parsers[parser.name] = parser

    def _register_source(self, source: dict):
        self.sources.append(source)

    def _fetch_sources(self) -> list:
        return [
            (source['title'], self.parsers[source['parser']], requests.get(source['url']).text)
            for source in self.sources
        ]

    def _parse_sources(self, as_dict=False) -> list:
        out = []

        for fetched_source in self._fetch_sources():
            news = fetched_source[1].parse(fetched_source[2], limit=self.config['news_limit'], as_dict=as_dict)
            if not as_dict:
                news.sort(key=lambda x: x.date, reverse=True)
            else:
                news.sort(key=lambda x: x['date'], reverse=True)
            out.append((fetched_source[0], news))

        return out
