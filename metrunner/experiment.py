from dataclasses import dataclass
from metrunner.algorithm import Algorithm
from metrunner.problem import Problem

@dataclass(frozen=True)
class Experiment:
    algorithm: Algorithm
    problem: Problem
    args: dict
    reps: int = 1

    def execute(self):
        for i in range(self.reps):
            print(f"Repetition # {i}")
            print(self.algorithm)
            print(self.problem)
