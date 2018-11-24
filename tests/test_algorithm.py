# Sample Test passing with nose and pytest
from metrunner.algorithm import Algorithm
import unittest


class TestAlgorithm(unittest.TestCase):

    def setUp(self):
        self.name = "MOEA/D"
        self.args = [200, 5, 6]
        self.algo = Algorithm(self.name, self.args)

    def test_algorithm_name(self):
        self.assertEqual(self.name, self.algo.name)

    def test_algorithm_args(self):
        self.assertEqual(len(self.args), len(self.algo.args))

    def test_algorithm_args_equals(self):
        for i in range(len(self.args)):
            self.assertEqual(self.args[i], self.algo.args[i])
