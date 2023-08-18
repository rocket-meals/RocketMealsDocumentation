from collections import OrderedDict

from RocketMealsDocumentation.hyper import tune_hyper_params

from .test_runners import env, cache_filename


def test_hyper(env):

    hyper_params = OrderedDict()
    hyper_params["popsize"] = [5]
    hyper_params["maxiter"] = [5, 10]
    hyper_params["method"] = ["uniform"]
    hyper_params["mutation_chance"] = [10]

    target_strategy = "genetic_algorithm"

    result = tune_hyper_params(target_strategy, hyper_params, *env, verbose=True, cache=cache_filename)
    assert len(result) > 0

