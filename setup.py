import setuptools

with open("README.md", "r", encoding = "utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name = "fast_sql",
    version = "0.0.5",
    author = "Farbod Parkhooi(Unknow-per)",
    author_email = "farbod.p1390@gmail.com",
    description = "Fast_sql is a library to use sqlite database faster and easier.",
    long_description = long_description,
    long_description_content_type = "text/markdown",
    url = "https://github.com/Unknow-per/Fast_SQL-lIbrary",
    project_urls = {
        "Bug Tracker": "https://github.com/Unknow-per/Fast_SQL-lIbrary/issues",
    },
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir = {"": "src"},
    packages = setuptools.find_packages(where="src"),
    python_requires = ">=3.9"
)