from dataclasses import dataclass, field
from typing import List
from metrunner.experiment import Experiment
from termcolor import cprint


@dataclass
class Runner:
    experiments: List[Experiment] = field(default_factory=list)

    def run_all(self):
        i = 1
        for exp in self.experiments:
            if exp.execute() is True:
                cprint(f"Experiment {i}/{len(self.experiments)} finished with exit", "green")
            else:
                cprint(f"Experiment {i}/{len(self.experiments)} failed. \n Aborted!", "red")
                return False
            i += 1

        return True

