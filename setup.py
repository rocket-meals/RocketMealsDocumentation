from setuptools import setup

setup(
    name="RocketMealsDocumentation",
    install_requires=[],
    extras_require={
        "doc": [
            "sphinx",
            "sphinx_rtd_theme",
            "nbsphinx",
            "pytest",
            "ipython",
            "markupsafe==2.0.1",
        ],
    },
)
