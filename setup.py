#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


readme = open('README.md').read()

requirements = [
    'wheel==0.23.0',
    'redis==2.8.0',
    'requests==1.2.3',
    'splinter'
]

test_requirements = [
]

setup(
    name='splinter_model',
    version='0.1.6',
    description='Splinter helper to create scrapers from models',
    long_description=readme,
    author='Bruno Rocha',
    author_email='rochacbruno@gmail.com',
    url='https://github.com/rochacbruno/splinter_model',
    py_modules=['splinter_model'],
    include_package_data=True,
    install_requires=requirements,
    license="BSD",
    zip_safe=False,
    keywords='splinter_model',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
