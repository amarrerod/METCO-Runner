from dataclasses import dataclass
from metrunner.algorithm import Algorithm
from metrunner.problem import Problem
from termcolor import cprint
from metrunner.constants import *
import subprocess, os


@dataclass(frozen=True)
class Experiment:
    algorithm: Algorithm
    problem: Problem
    args: dict
    reps: int = 1

    def execute(self):
        if self.sanity_checks():
            for i in range(self.reps):
                if not os.path.exists(self.args[OUTPUT_PATH]):
                    os.mkdir(self.args[OUTPUT_PATH])
                file = f"{self.args[OUTPUT_FILE]}_{i}.rs"
                run_cmd = self.create_command([METCO_SEQ, self.args[OUTPUT_PATH],
                                               self.args[PLUGIN_PATH], self.args[PRINTER],
                                               file, self.algorithm.name,
                                               self.problem.name, self.args[STOP],
                                               self.args[STOP_VALUE],
                                               self.args[PRINT_PERIOD], self.args[EXTERNAL_FILE], " "])
                if int(self.args[EXTERNAL_FILE] != NOT_EXTERNAL_FILE):
                    pass
                run_cmd += ' '.join(self.algorithm.args)
                if self.problem.args:
                    run_cmd += self.create_command([" ", PROBLEM_ESCAPE, " "])
                    run_cmd += self.create_command(self.problem.args)
                    run_cmd += " "
                if all(k in self.args for k in (MUTATION, CROSSOVER)):
                    run_cmd += self.create_command([MUTATION_ESCAPE,
                                                    self.args[MUTATION],
                                                    self.args[CROSSOVER]])
                if LOCAL_SEARCH in self.args:
                    run_cmd += self.create_command([LS_ESCAPE, " "])
                    run_cmd += self.args[LOCAL_SEARCH]
                    run_cmd += " "
                if MULTIOBJS in self.args:
                    run_cmd += self.create_command(MUTATION_ESCAPE)
                    run_cmd += self.create_command(self.args[MULTIOBJS])
                if DECOMPOSITION in self.args:
                    run_cmd += self.create_command([DECOM_ESCAPE, " "])
                    run_cmd += self.args[DECOMPOSITION]
                print(f"About to run: {run_cmd}")
                result = subprocess.run(run_cmd, shell=True)
                if result.returncode == 0:
                    cprint(f"Repetition #{i} of the experiment {self.algorithm.name}"
                           f"_{self.problem.name} finished", "green")
                else:
                    cprint(f"Repetition #{i} of the experiment {self.algorithm.name}"
                           f" {self.problem.name} finished wrong. Aborting experiment", "red")
                    return False
            return True

        else:
            return False

    def sanity_checks(self):
        if all(k in self.args for k in (PLUGIN_PATH, PRINTER, OUTPUT_PATH,
                                        STOP, STOP_VALUE, PRINT_PERIOD,
                                        EXTERNAL_FILE, LOCAL_SEARCH)):
            return True
        else:
            return False

    @staticmethod
    def create_command(params):
        return " ".join(params)
