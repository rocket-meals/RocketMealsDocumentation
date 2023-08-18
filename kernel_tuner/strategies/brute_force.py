""" The default strategy that iterates through the whole parameter space """
from RocketMealsDocumentation.searchspace import Searchspace
from RocketMealsDocumentation.strategies import common

_options = {}

def tune(searchspace: Searchspace, runner, tuning_options):

    # call the runner
    return runner.run(searchspace.sorted_list(), tuning_options)


tune.__doc__ = common.get_strategy_docstring("Brute Force", _options)
