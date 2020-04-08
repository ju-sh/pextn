import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pextn",
    version="0.1",
    author="Julin S",
    author_email="julins@cannottellyou.yet",
    description="A simple, lazy utility to display information about a file extension.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ju-sh/pextn",
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    classifiers=[
        # https://pypi.org/pypi?%3Aaction=list_classifiers
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Utilities",
        "Development Status :: 2 - Pre-Alpha",
        "Natural Language :: English",
    ],
    project_urls={
        #'Changelog': 'https://github.com/user/project/CHANGELOG.rst',
        'Issue Tracker': 'https://github.com/ju-sh/pextn/issues',
    },
    install_requires=[],
    python_requires='>=3.6',
)
