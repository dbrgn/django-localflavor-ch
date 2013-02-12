# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import meta

README = open('README.rst').read()

setup(
    name = meta.name,
    version = meta.version,
    description = 'Country-specific Django helpers for %s.' % meta.country,
    long_description = README,
    author = 'Django Software Foundation',
    author_email = 'foundation@djangoproject.com',
    license='BSD',
    url = 'https://github.com/django/%s' % meta.name,
    packages = find_packages(),
    package_data = {
        '': ['locale/*/*/*.mo', 'locale/*/*/*.po'],
    },
    zip_safe=False,
    keywords='django localflavor %s' % meta.country.lower(),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    install_requires=['Django>=1.4']
)
