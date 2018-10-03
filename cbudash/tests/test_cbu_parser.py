#!/usr/bin/env python3

import base64
import datetime
import unittest

from cbudash.data import NewsItem

from cbudash.parser import CBUParser


def get_src_cse_home():
    with open('./.cse_home.b64', 'r') as f:
        return base64.b64decode(f.read())


class TestCbuParser(unittest.TestCase):

    def setUp(self):
        super().setUp()
        self.parser = CBUParser()

    def test_parser_name_is_correct(self):
        self.assertEqual(self.parser.name, 'CBUParser')

    def test_parser_returns_empty_list_for_empty_input(self):
        self.assertEqual(len(self.parser.parse('')), 0)

    def test_parser_returns_non_empty_list_for_cse_homepage(self):
        self.assertGreater(len(self.parser.parse(get_src_cse_home())), 0)

    def test_parser_returns_list_of_news_items(self):
        items = self.parser.parse(get_src_cse_home())
        self.assertEqual(type(NewsItem(None, None, None, None)), type(items[0]))

    def test_parsers_parses_first_news_item_correctly(self):
        first_item = self.parser.parse(get_src_cse_home())[0]

        self.assertEqual(first_item.category, 'Genel')
        self.assertEqual(first_item.title, 'CSE 3246 Cyber Security Dersi ile İlgili!')
        self.assertEqual(
            first_item.url,
            'http://bilgisayarmuh.cbu.edu.tr/db_images/site_111/file/cse-3246-cyber-securitydersiptal.pdf'
        )
        self.assertEqual(
            first_item.date.strftime('%Y-%m-%d'),
            datetime.datetime(year=2018, month=10, day=1).date().strftime('%Y-%m-%d')
        )

    def test_parser_obeys_the_item_number_limit(self):
        items = self.parser.parse(get_src_cse_home(), limit=10)
        self.assertEqual(len(items), 10)
