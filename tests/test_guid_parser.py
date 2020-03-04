# -*- coding: utf-8 -*-
import unittest

from etl.parsers.etw.core import guid, Guid


class GuidParser(unittest.TestCase):
    """
    Test the Global Unique Identifier parser
    """
    def test_guid_parser(self):
        a = guid("2ed6006e-4729-4609-b423-3ee7bcd678ef")
        b = Guid(785776750, 18217, 17929, [180, 35, 62, 231, 188, 214, 120, 239])
        self.assertEqual(a, b)
