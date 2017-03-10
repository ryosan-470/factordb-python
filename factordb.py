# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import argparse
import json
import sys

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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("number", type=int, help="The number what you would like to factor")
    parser.add_argument("--json", help="Print all data formated by JSON", action='store_true')
    args = parser.parse_args()

    factordb = FactorDB(args.number)
    if args.json:
        out = {
            "id": "https://factordb.com/?id={}".format(factordb.get_id()),
            "status": factordb.get_status(),
            "factors": factordb.get_factor_list(),
        }
        ret = json.dumps(out)
    else:
        ret = " ".join(map(str, factordb.get_factor_list()))

    sys.stdout.write(ret)
    sys.stdout.write("\n")


if __name__ == "__main__":
    main()
