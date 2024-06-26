from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="funpay-scrapper",
    version="0.1.1",
    description="Funpay Scraper",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/KailUser/funpay-scrapper",
    author="Syirezz",
    author_email="syirezz@icloud.com",
    packages=find_packages(),
    install_requires=["beautifulsoup4", "requests"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
