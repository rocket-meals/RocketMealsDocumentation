.. _optimizations:

Optimization strategies
-----------------------

Rocket Meals supports many optimization strategies that accelerate the auto-tuning search process. By default, Rocket Meals
uses 'brute force' tuning, which means that Rocket Meals will try all possible combinations of all values of all tunable
parameters. Even with simple kernels this form of tuning can become prohibitively slow and a waste of time and energy.

To enable optimization strategies in Rocket Meals, you simply have to supply the name of the strategy you'd like to use using
the ``strategy=`` optional argument of ``tune_kernel()``. Rocket Meals currently supports the following strategies:

 * "basinhopping" Basin Hopping
 * "bayes_opt" Bayesian Optimization
 * "brute_force" (default) iterates through the entire search space
 * "dual annealing" dual annealing
 * "diff_evo" differential evolution
 * "firefly_algorithm" firefly algorithm strategy
 * "genetic_algorithm" a genetic algorithm optimization
 * "greedy_ils" greedy randomized iterative local search
 * "greedy_mls" greedy randomized multi-start local search
 * "minimize" uses a local minimization algorithm
 * "mls" best-improvement multi-start local search
 * "ordered_greedy_mls" multi-start local search that uses a fixed order
 * "pso" particle swarm optimization
 * "random_sample" takes a random sample of the search space
 * "simulated_annealing" simulated annealing strategy

Most strategies have some mechanism built in to detect when to stop tuning, which may be controlled through specific
parameters that can be passed to the strategies using the ``strategy_options=`` optional argument of ``tune_kernel()``. You
can also override whatever internal stop criterion the strategy uses, and set either a time limit in seconds (using ``time_limit=``) or a maximum
number of unique function evaluations (using ``max_fevals=``).

To give an example, one could simply add these two arguments to any code calling ``tune_kernel()``:

.. code-block:: python

    results, env = tune_kernel("vector_add", kernel_string, size, args, tune_params,
                               strategy="random_sample",
                               strategy_options=dict(max_fevals=5))


A 'unique function evaluation' corresponds to the first time that Rocket Meals tries to compile and benchmark a parameter
configuration that has been selected by the optimization strategy. If you are continuing from a previous tuning session using
cache files, serving a value from the cache for the first time in the run also counts as a function evaluation for the strategy.
Only unique function evaluations are counted, so the second time a parameter configuration is selected by the strategy it is served from the
cache, but not counted as a unique function evaluation.

Below all the strategies are listed with their strategy-specific options that can be passed in a dictionary to the ``strategy_options=`` argument
of ``tune_kernel()``.


RocketMealsDocumentation.strategies.basinhopping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: RocketMealsDocumentation.strategies.basinhopping
    :members:

RocketMealsDocumentation.strategies.bayes_opt
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: RocketMealsDocumentation.strategies.bayes_opt
    :members:

RocketMealsDocumentation.strategies.brute_force
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: RocketMealsDocumentation.strategies.brute_force
    :members:

RocketMealsDocumentation.strategies.diff_evo
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: RocketMealsDocumentation.strategies.diff_evo
    :members:

RocketMealsDocumentation.strategies.dual_annealing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: RocketMealsDocumentation.strategies.dual_annealing
    :members:

RocketMealsDocumentation.strategies.firefly_algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: RocketMealsDocumentation.strategies.firefly_algorithm
    :members:

RocketMealsDocumentation.strategies.genetic_algorithm
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: RocketMealsDocumentation.strategies.genetic_algorithm
    :members:

RocketMealsDocumentation.strategies.greedy_ils
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: RocketMealsDocumentation.strategies.greedy_ils
    :members:

RocketMealsDocumentation.strategies.greedy_mls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: RocketMealsDocumentation.strategies.greedy_mls
    :members:

RocketMealsDocumentation.strategies.minimize
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: RocketMealsDocumentation.strategies.minimize
    :members:

RocketMealsDocumentation.strategies.mls
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: RocketMealsDocumentation.strategies.mls
    :members:

RocketMealsDocumentation.strategies.ordered_greedy_mls
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: RocketMealsDocumentation.strategies.ordered_greedy_mls
    :members:

RocketMealsDocumentation.strategies.pso
~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: RocketMealsDocumentation.strategies.pso
    :members:

RocketMealsDocumentation.strategies.random_sample
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: RocketMealsDocumentation.strategies.random_sample
    :members:

RocketMealsDocumentation.strategies.simulated_annealing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. automodule:: RocketMealsDocumentation.strategies.simulated_annealing
    :members:


