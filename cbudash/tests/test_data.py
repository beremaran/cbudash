#!/usr/bin/env python3

import json
import unittest
from datetime import date

from cbudash.data import NewsItem


def get_test_news_item():
    _date = date.today()
    _category = 'Category'
    _title = 'Title'
    _url = 'https://google.com'

    return _date, _category, _title, _url, NewsItem(date=_date, category=_category, title=_title, url=_url)


class TestData(unittest.TestCase):
    def test_constructor_is_setting_news_item_fields(self):
        _date, _category, _title, _url, item = get_test_news_item()

        self.assertEqual(item.date, _date)
        self.assertEqual(item.category, _category)
        self.assertEqual(item.title, _title)
        self.assertEqual(item.url, _url)

    def test_to_dict_method_has_all_fields(self):
        _date, _category, _title, _url, item = get_test_news_item()
        item_dict = item.to_dict()

        self.assertTrue('date' in item_dict.keys())
        self.assertTrue('category' in item_dict.keys())
        self.assertTrue('title' in item_dict.keys())
        self.assertTrue('url' in item_dict.keys())

    def test_str_is_json_equivalent_of_to_dict_method(self):
        _date, _category, _title, _url, item = get_test_news_item()
        item_dict = item.to_dict()

        self.assertEqual(json.dumps(item_dict), str(item))
