import unittest
from metrunner.parser import input_parser


class TestInputParser(unittest.TestCase):

    def setUp(self):
        self.file = "inputs/input_1.json"
        self.exps = input_parser(self.file)

    def test_exps_len(self):
        self.assertEqual(len(self.exps), 1)