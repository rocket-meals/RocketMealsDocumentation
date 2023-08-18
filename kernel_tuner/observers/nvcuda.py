import numpy as np

try:
    from cuda import cudart
except ImportError:
    cuda = None

from RocketMealsDocumentation.observers.observer import BenchmarkObserver
from RocketMealsDocumentation.util import cuda_error_check


class CudaRuntimeObserver(BenchmarkObserver):
    """Observer that measures time using CUDA events during benchmarking"""

    def __init__(self, dev):
        self.dev = dev
        self.stream = dev.stream
        self.start = dev.start
        self.end = dev.end
        self.times = []

    def after_finish(self):
        # Time is measured in milliseconds
        err, time = cudart.cudaEventElapsedTime(self.start, self.end)
        cuda_error_check(err)
        self.times.append(time)

    def get_results(self):
        results = {"time": np.average(self.times), "times": self.times.copy()}
        self.times = []
        return results
