from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# TODO Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='coindesk',
    version='0.0.1a1',
    description='This library fetches Coindesk\'s Bitcoin Price Index from their API.',
    long_description=long_description,
    url='https://github.com/L-Cafe/Coindesk-Python-API-client',
    author='L-Cafe',
    author_email='L-Cafe@linux.com',
    license='GPLv3',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='bitcoin coindesk bpi price',
    install_requires=['requests']
    # TODO You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    #packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # TODO Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],

    # TODO List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    #extras_require={
    #    'dev': ['check-manifest'],
    #    'test': ['coverage'],
    #},

    # TODO To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    #entry_points={
    #    'console_scripts': [
    #        'sample=sample:main',
    #    ],
    #},
)
