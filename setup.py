import os
import sys
from pathlib import Path
from shutil import rmtree

from setuptools import Command, find_packages, setup

# Package meta-data.

NAME = "html-dsl"
DESCRIPTION = "A HTML-DSL for Python"
URL = "https://github.com/duyixian1234/html_dsl"
EMAIL = "duyixian1234@qq.com"
AUTHOR = "Yixian Du"

# What packages are required for this module to be executed?


here = Path(__file__).cwd()

with open(here / "README.rst", encoding="utf-8") as f:
    long_description = "\n" + f.read()


class UploadCommand(Command):
    """Support setup.py upload."""

    description = "Build and publish the package."
    user_options: list = []

    @staticmethod
    def status(s):
        """Prints things in bold."""
        print("\033[1m{0}\033[0m".format(s))

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        try:
            self.status("Removing previous builds…")
            rmtree(here / "dist")
        except OSError:
            pass

        self.status("Building Source and Wheel (universal) distribution…")
        os.system("{0} setup.py sdist bdist_wheel".format(sys.executable))
        self.status("Uploading the package to PyPi via Twine…")
        os.system("twine upload dist/*")
        sys.exit()


setup(
    name=NAME,
    version="0.1.0",
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=find_packages(exclude=("tests",)),
    entry_points={},
    install_requires=[],
    include_package_data=True,
    license="MIT",
    classifiers=[
        # Trove classifiers
        # Full list: https://pypi.python.org/pypi?%3Aaction=list_classifiers
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: Implementation :: CPython",
    ],
    # $ setup.py publish support.
    cmdclass={"upload": UploadCommand},
)
