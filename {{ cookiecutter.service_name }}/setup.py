from setuptools import setup, find_packages
import codecs
import os


# get current directory
here = os.path.abspath(os.path.dirname(__file__))


def get_long_description():
    """
    get long description from README.rst file
    """
    with codecs.open(os.path.join(here, "README.rst"), "r", "utf-8") as f:
        return f.read()


setup(
    name="{{ cookiecutter.service_name }}",
    version="{{ cookiecutter.version }}",
    description="{{ cookiecutter.url }}",
    long_description=get_long_description(),
    url="{{ cookiecutter.url }}",
    author="{{ cookiecutter.author }}",
    author_email="{{ cookiecutter.email }}",
    license="MIT",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="python packaging",
    packages=find_packages(
        exclude=["contrib", "docs", "tests"]
    ),
    entry_points = {
        "console_scripts": [
            "{{ cookiecutter.service_name }}={{ cookiecutter.service_name }}.manage:cli"
        ],
    },
    install_requires=[
        "fastapi", "uvicorn[standard]", "argon2-cffi", "passlib", 
        "pyyaml", "sqlalchemy", "alembic", "sqla-yaml-fixtures", 
        "python-jose", "python-multipart"
    ]
)
