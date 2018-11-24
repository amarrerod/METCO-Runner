import unittest
from metrunner.experiment import Experiment
from metrunner.problem import Problem
from metrunner.algorithm import Algorithm


class TestExperiment(unittest.TestCase):

    def setUp(self):
        self.reps = 1
        self.algo = Algorithm("MOEA/D", [200, 5, 20])
        self.problem = Problem("Rastrigin", [30])
        self.args = {
            "plugin_path": "here",
            "printer": "PlainText"
        }
        self.exp = Experiment(self.algo, self.problem, self.args, self.reps)

    def test_experiment_reps(self):
        self.assertEqual(self.exp.reps, self.reps)

    def test_experiment_algo(self):
        self.assertEqual(self.algo, self.exp.algorithm)

    def test_experiment_problem(self):
        self.assertEqual(self.problem, self.exp.problem)

    def test_experiment_args(self):
        self.assertDictEqual(self.args, self.exp.args)

    def test_experiment_exec(self):
        self.assertTrue(self.exp.execute())
