import re
from setuptools import setup


def version():
    with open("RocketMealsDocumentation/__init__.py") as fp:
        match = re.search(r"__version__\s*=\s*['\"]([^'\"]+)", fp.read())

    if not match:
        raise RuntimeError("unable to find __version__ string in __init__.py")

    return match[1]


def readme():
    with open("README.rst") as f:
        return f.read()


setup(
    name="RocketMealsDocumentation",
    version=version(),
    author="Ben van Werkhoven",
    author_email="b.vanwerkhoven@esciencecenter.nl",
    description=("An easy to use CUDA/OpenCL kernel tuner in Python"),
    license="Apache 2.0",
    keywords="auto-tuning gpu computing pycuda cuda pyopencl opencl",
    url="https://rocket-meals.github.io/RocketMealsDocumentation/",
    include_package_data=True,  # use MANIFEST.in during install
    project_urls={
        "Documentation": "https://rocket-meals.github.io/RocketMealsDocumentation/",
        "Source": "https://github.com/rocket-meals/RocketMealsDocumentation",
        "Tracker": "https://github.com/rocket-meals/RocketMealsDocumentation/issues",
    },
    packages=[
        "RocketMealsDocumentation",
        "RocketMealsDocumentation.backends",
        "RocketMealsDocumentation.energy",
        "RocketMealsDocumentation.observers",
        "RocketMealsDocumentation.runners",
        "RocketMealsDocumentation.strategies",
    ],
    long_description=readme(),
    long_description_content_type="text/x-rst",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
        "License :: OSI Approved :: Apache Software License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Topic :: Scientific/Engineering",
        "Topic :: Software Development",
        "Topic :: System :: Distributed Computing",
        "Development Status :: 5 - Production/Stable",
    ],
    install_requires=[
        "numpy>=1.13.3,<1.24.0",
        "scipy>=1.8.1",
        "jsonschema",
        "python-constraint",
        "xmltodict",
    ],
    extras_require={
        "doc": [
            "sphinx",
            "sphinx_rtd_theme",
            "nbsphinx",
            "pytest",
            "ipython",
            "markupsafe==2.0.1",
        ],
        "cuda": ["pycuda", "nvidia-ml-py", "pynvml>=11.4.1"],
        "opencl": ["pyopencl"],
        "cuda_opencl": ["pycuda", "pyopencl"],
        "tutorial": ["jupyter", "matplotlib", "pandas"],
        "dev": [
            "numpy>=1.13.3",
            "scipy>=0.18.1",
            "mock>=2.0.0",
            "pytest>=3.0.3",
            "Sphinx>=1.4.8",
            "scikit-learn>=0.24.2",
            "scikit-optimize>=0.8.1",
            "sphinx-rtd-theme>=0.1.9",
            "nbsphinx>=0.2.13",
            "jupyter>=1.0.0",
            "matplotlib>=1.5.3",
            "pandas>=0.19.1",
            "pylint>=1.7.1",
            "bayesian-optimization>=1.0.1",
        ],
    },
)
