from dataclasses import dataclass, field
from typing import List
from metrunner.experiment import Experiment


@dataclass
class Runner:
    experiments: List[Experiment] = field(default_factory=list)

    def run_all(self):
        for exp in self.experiments:
            exp.execute()


