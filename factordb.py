# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import requests


ENDPOINT = "https://factordb.com/api"


class FactorDB():
    def __init__(self, n):
        self.n = n
        self.r = requests.get(ENDPOINT, params={"query": str(self.n)})

    def get_id(self):
        return self.r.json().get("id")

    def get_status(self):
        return self.r.json().get("status")

    def get_factor_from_api(self):
        factors = self.r.json().get("factors")
        return factors

    def get_factor_list(self):
        """
        get_factors: [['2', 3], ['3', 2]]
        Returns: [2, 2, 2, 3, 3]
        """
        ml = [[int(x)] * y for x, y in self.get_factor_from_api()]
        return [y for x in ml for y in x]
