import pathlib
from setuptools import setup, find_packages


def get_long_description():
    # TODO: what is resolve, why encode, what is utf-8, how to return it
    here = pathlib.Path(__file__).parent.resolve()
    return (here / "README.md").read_text(encoding="utf-8")


setup(
    name="law-crawler",
    version="0.0.1",
    author="Dazzy Dan",
    description="Law website crawler",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    url="https://github.com/DazzyDan/Law-crawler.git",
    package_dir={"": "src"},
    python_requires=">3.8",
    packages=find_packages(where="src"),
    install_requires=[
        "Flask==2.1.1",
        "gunicorn==20.0.4",
        "lxml==4.9.1",
        "numpy==1.23.4",
        "openpyxl==3.0.10",
        "packaging==21.3",
        "pandas==1.5.1",
        "requests==2.28.1",
        "selenium==4.5.0",
        "urllib3==1.26.12",
        "gevent",
    ],
    # TODO: how to test
    extras_require={
        "test": [
            "coverage",
            "pycodestyle",
            "black==22.10.0",
        ]
    },
    entry_points={"console_scripts": ["law_crawler=law_crawler.cli.server:main"]},
)
