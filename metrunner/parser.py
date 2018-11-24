import json
from metrunner.algorithm import Algorithm
from metrunner.problem import Problem
from metrunner.experiment import Experiment
from metrunner.constants import *


def input_parser(input_file):
    exps = list()
    with open(input_file) as file:
        data = json.load(file)
        for ex in data[EXPERIMENTS]:
            algo = Algorithm(ex[ALGORITHM][NAME], ex[ALGORITHM][ARGS])
            prob = Problem(ex[PROBLEM][NAME], ex[PROBLEM][ARGS])
            exps.append(Experiment(algo, prob, ex[ARGS], ex[REPS]))
    return exps
