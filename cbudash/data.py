#!/usr/bin/env python3

import json
import datetime


class NewsItem:
    def __init__(self, date: datetime.date, category: str, title: str, url: str):
        self.date = date
        self.category = category
        self.title = title
        self.url = url

    def to_dict(self):
        return {
            'date': self.date.strftime('%Y-%m-%d'),
            'category': self.category,
            'title': self.title,
            'url': self.url
        }

    def __str__(self):
        return json.dumps(self.to_dict())


class NewsGroup(list):
    def __init__(self):
        super().__init__()

    def to_dict(self):
        return [n.to_dict() for n in self]
