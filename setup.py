import os

from setuptools import setup, find_packages
from version import __version__

# Pull version from source without importing
# since we can't import something we haven't built yet :)
exec(open('version.py').read())

here = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(here, 'README.md')) as f:
    README = f.read()

setup(
    name="python-library",
    version=__version__,
    author="Dana Powers",
    author_email="dana.powers@gmail.com",
    url="https://github.com/singhania94/python-learn",
    license="Apache License 2.0",
    description="Pure Python useless library",
    long_description=README,
    keywords="learning python",
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    pythonrequires='>=3',
    install_requires=['kafka-python'],
    # extras_require={
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    # },
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)


