# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import argparse
import json
import sys

from .factordb import FactorDB, ENDPOINT


def create_parser():
    parser = argparse.ArgumentParser(
        description="The CLI for factordb.com"
    )

    parser.add_argument(
        "number",
        type=int,
        help="The number what you want to factor"
    )

    parser.add_argument(
        "--json",
        help="Print all data formated by JSON",
        action='store_true'
    )

    return parser


def main():
    parser = create_parser()
    args = parser.parse_args()

    factordb = FactorDB(args.number)
    factordb.connect()

    if args.json:
        out = {
            "id": "{}/?id={}".format(ENDPOINT, factordb.get_id()),
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
