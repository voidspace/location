import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="location",
    version="0.1.0",
    author="Michael Foord",
    author_email="michael@python.org",
    description="A package for working with distances",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/voidspace/location",
    packages=setuptools.find_packages(),
    package_data={'location': ['*.csv']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3.0 or later (GPL-3.0-or-later)",
        "Operating System :: OS Independent",
    ],
)