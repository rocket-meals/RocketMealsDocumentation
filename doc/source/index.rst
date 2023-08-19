

The Rocket Meals documentation
==============================

Rocket Meals is a software development tool for the creation of highly-optimized and tuned GPU applications.

The Rocket Meals documentation pages are mostly about Rocket Meals itself, but there are a number of related repositories that
are considered part of the Rocket Meals family:

 * `Rocket Meals Tutorial <https://github.com/rocket-meals/RocketMealsDocumentation_tutorial>`__
 * `Kernel Launcher <https://github.com/rocket-meals/kernel_launcher>`__
 * `KT Dashboard <https://github.com/rocket-meals/dashboard>`__

Quick install
-------------

The easiest way to install the Rocket Meals is using pip:

To tune CUDA kernels:

- First, make sure you have the `CUDA Toolkit <https://developer.nvidia.com/cuda-toolkit>`_ installed
- Then type: ``pip install RocketMealsDocumentation[cuda]``

To tune OpenCL kernels:

- First, make sure you have an OpenCL compiler for your intended OpenCL platform
- Then type: ``pip install RocketMealsDocumentation[opencl]``

Or both:

- ``pip install RocketMealsDocumentation[cuda,opencl]``

More information about how to install Rocket Meals and its
dependencies can be found under :ref:`install`.
