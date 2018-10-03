#!/usr/bin/env python3

import time


def get_timestamp():
    return int(time.time())


class RequestCache:
    def __init__(self):
        self.cache = {}

    def has(self, key: str) -> bool:
        return hash(key) in self.cache.keys()

    def set(self, key: str, value: any, lifetime: int = 360):
        self.cache[hash(key)] = {
            'expires_at': get_timestamp() + lifetime,
            'data': value
        }

    def get(self, key: str, default=None):
        if not self.has(key):
            return default

        hashed_key = hash(key)
        # check if expired
        if get_timestamp() >= self.cache[hashed_key]['expires_at']:
            del self.cache[hashed_key]
            return default

        return self.cache[hashed_key]['data']
