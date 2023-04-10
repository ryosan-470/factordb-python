# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals
import unittest

from factordb.factordb import FactorDB
from Crypto.Util import number


class FactorDBTestCase(unittest.TestCase):
    def test_factordb_api_1(self):
        factordb = FactorDB(1)
        factordb.connect()

        self.__check_testcase(factordb, {
            'id': -1,
            'status': "Unit",
            'factors': []
        })

        self.assertFalse(factordb.is_prime())

    def test_factordb_api_16(self):
        factordb = FactorDB(16)
        factordb.connect()

        self.__check_testcase(factordb, {
            'id': '2',
            'status': 'FF',
            'factors': [2, 2, 2, 2]
        })

        self.assertFalse(factordb.is_prime())

    def test_factordb_api_large_composite_number(self):
        """
        Large composite number tests from RSA 768 challenges
        """
        p = int("3347807169895689878604416984821269081770479498371376856891243"
                "1388982883793878002287614711652531743087737814467999489")
        q = int("3674604366679959042824463379962795263227915816434308764267603"
                "2283815739666511279233373417143396810270092798736308917")

        factordb = FactorDB(p * q)
        factordb.connect()

        self.__check_testcase(factordb, {
            'id': '1100000000193442616',
            'status': 'FF',
            'factors': [p, q]
        }
        )

        self.assertFalse(factordb.is_prime())

    def test_factordb_api_prime(self):
        factordb = FactorDB(7)
        factordb.connect()

        self.__check_testcase(factordb, {
            'id': '7',
            'status': 'P',
            'factors': [7]
        })

        self.assertTrue(factordb.is_prime())

    def test_submit(self):
        def generate_unfactorised_nums():
            p = number.getPrime(1024)
            q = number.getPrime(1024)
            n = p * q

            factordb = FactorDB(n)
            factordb.connect()

            if factordb.get_status() == 'C':
                return n, sorted([p, q])

            return generate_unfactorised_nums()

        n, factors = generate_unfactorised_nums()
        FactorDB.submit_factors(n, factors)

        factordb = FactorDB(n)
        factordb.connect(reconnect=True)
        self.assertEqual(factordb.get_status(), 'FF')
        self.assertListEqual(factordb.get_factor_list(), factors)

    def __check_testcase(self, factordb, expected):
        self.assertEqual(factordb.get_id(), expected['id'])
        self.assertEqual(factordb.get_status(), expected['status'])
        self.assertListEqual(factordb.get_factor_list(), expected['factors'])
