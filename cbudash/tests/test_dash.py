#!/usr/bin/env python3

import unittest

from cbudash.dash import CBUDash


class TestDash(unittest.TestCase):
    def setUp(self):
        super().setUp()
        self.dash = CBUDash('./config.json')

    def test_sources_has_titles(self):
        sources = self.dash.sources

        for source in sources:
            self.assertTrue('title' in source.keys())

    def test_dash_is_separating_sources(self):
        data = self.dash.get()
        sources = self.dash.sources
        source_titles = [source['title'] for source in sources]

        self.assertEqual(len(data), len(sources))

        for parsed_source in data:
            self.assertIn(parsed_source[0], source_titles)

    def test_dash_is_sorting_news(self):
        data = self.dash.get()

        for parsed_source in data:
            for i in range(len(parsed_source[1]) - 1):
                self.assertTrue(parsed_source[1][i].date >= parsed_source[1][i + 1].date)
