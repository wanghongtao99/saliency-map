#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
from utils import *


class OpencvIoTest(unittest.TestCase):
    def setUp(self):
        self.oi = OpencvIo()
        self.__img_path = './images/fruit.jpg'

    def test_imread(self):
        self.assertIsNotNone(self.oi.imread(self.__img_path))


class UtilTest(unittest.TestCase):
    def setUp(self):
        self.util = Util()

    def test_normalize_range(self):
        numss = [[1, 2], [3, 4], [5, 6]]
        tenss = [[10, 20], [30, 40], [50, 60]]
        self.assertEqual(tenss, self.util.normalize_range(numss, 10, 60))
        self.assertEqual([[5, 5], [5, 5]], self.util.normalize_range([[1, 1], [1, 1]], 0, 10))

    def test_normalize(self):
        numss = [[1, 1, 1], [1, 10, 1], [1, 1, 1]]
        expect = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
        self.assertTrue(np.array_equal(expect, self.util.normalize(numss)))


def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(OpencvIoTest))
    suite.addTests(unittest.makeSuite(UtilTest))
    return suite
