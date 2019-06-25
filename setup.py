from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="bg.ai",
    version="0.0.1",
    author="thundercrawl",
    author_email="brightpegion@gmail.com",
    description="AI tutorial",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thundercrawl/pythonAI",
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
) 