#!/usr/bin/env python
""" This is the example demonstrates how to use Rocket Meals
    to insert tunable parameters into template arguments
"""

import json
import numpy
from RocketMealsDocumentation import tune_kernel

def tune():

    kernel_string = """
template<typename T, int blockSize>
__global__ void vector_add(T *c, T *a, T *b, int n) {
    auto i = blockIdx.x * blockSize + threadIdx.x;
    if (i<n) {
        c[i] = a[i] + b[i];
    }
}
"""

    size = 10000000

    a = numpy.random.randn(size).astype(numpy.float32)
    b = numpy.random.randn(size).astype(numpy.float32)
    c = numpy.zeros_like(b)
    n = numpy.int32(size)

    args = [c, a, b, n]

    tune_params = dict()
    tune_params["block_size_x"] = [128+64*i for i in range(15)]

    result, env = tune_kernel("vector_add<float, block_size_x>", kernel_string, size, args, tune_params)

    with open("vector_add.json", 'w') as fp:
        json.dump(result, fp)

    return result


if __name__ == "__main__":
    tune()
