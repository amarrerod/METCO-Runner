from dataclasses import dataclass
from metrunner.algorithm import Algorithm
from metrunner.problem import Problem
from termcolor import cprint

@dataclass(frozen=True)
class Experiment:
    algorithm: Algorithm
    problem: Problem
    args: dict
    reps: int = 1

    def execute(self):
        for i in range(self.reps):
            print(self.algorithm)
            print(self.problem)
            cprint(f"Repetition #{i} of the experiment {self.algorithm.name}"
                   f"_{self.problem.name} finished", "green")
            return True
