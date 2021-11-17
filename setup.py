import pathlib
from setuptools import setup, find_packages

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name="m6",
    version="0.0.3",
    description="Utilities for M6 Financial Forecasting Competition",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/microprediction/m6",
    author="microprediction",
    author_email="peter.cotton@microprediction.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    packages=["m6","m6.bruteforce"],
    test_suite='pytest',
    tests_require=['pytest','microprediction'],
    include_package_data=True,
    install_requires=["wheel","pathlib","numpy","scikit-learn","runthis","freelunch"],
    entry_points={
        "console_scripts": [
            "m6=m6.__main__:main",
        ]
    },
)
