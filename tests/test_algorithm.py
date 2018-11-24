# Sample Test passing with nose and pytest
from metrunner.algorithm import Algorithm

empty_params = Algorithm("MOEA/D", [])
params = [5, 200, 5]
algo = Algorithm("MOEA/D", params)

def test_pass():
    assert True, "dummy sample test"


def test_algorithm_name():
    assert "MOEA/D", empty_params.name


def test_algorithm_params():
      assert params, algo.params