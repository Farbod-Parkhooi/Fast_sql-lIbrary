import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fast_sql-Unknow-per", # Replace with your own username
    version="1.0.0",
    author="Farbod Parkhooi",
    author_email="farbod.p1390@gmail.com",
    description="This is a Python library to make and use a Sqlite databse easier and faster!",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Unknow-per/Fast_sqlite-Library",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)