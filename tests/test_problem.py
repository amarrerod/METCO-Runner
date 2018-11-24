import unittest
from metrunner.problem import Problem


class TestProblem(unittest.TestCase):

    def setUp(self):
        self.name = "Rastrigin"
        self.args = [5]
        self.problem = Problem(self.name, self.args)

    def test_name(self):
        self.assertEqual(self.name, self.problem.name)

    def test_args(self):
        self.assertEqual(len(self.problem.args), len(self.args))

    def test_args_equal(self):
        self.assertEqual(self.problem.args[0], self.args[0])
