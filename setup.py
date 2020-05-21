#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', 'pymongo', 'dnspython', 'pyyaml']

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Danylo Lykov",
    author_email='lkvdan@gmail.com',
    python_requires='>=3.5',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],

    description="Cli tool to interact with mongodb",
    entry_points={
        'console_scripts': [
            'mongocat=mongocat.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='mongocat',
    name='mongocat',
    packages=find_packages(include=['mongocat', 'mongocat.*']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/DaniloZZZ/mongocat',
    version='0.1.2',
    zip_safe=False,
)
