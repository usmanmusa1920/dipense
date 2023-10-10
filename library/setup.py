# -*- coding: utf-8 -*-
import re
import os
from setuptools import setup
from setuptools import find_packages


def grep(attrname):
    """get package info from __init__.py file"""
    file_path = os.path.join(os.path.dirname(__file__), 'dipense/__init__.py')

    # content of the file
    read_file = open(file_path).read()

    # pattern match using regex
    pattern = r"{0}\W*=\W*'([^']+)'".format(attrname)

    # our regex value
    attr_value, = re.findall(pattern, read_file)
    return attr_value


setup(
    name = grep('__title__'), # name of the main package (base folder i.e dipense)
    version = grep('__version__'),
    description = grep('__description__'),
    long_description = open('README.md').read() + '\n\n' + open('CHANGELOG').read(),
    long_description_content_type='text/markdown',
    python_requires = '>=3.7',
    platforms='any',

    url = grep('__url__'),
    download_url = grep('__download_url__'),
    author = grep('__author__'),
    author_email = grep('__author_email__'),
    license = grep('__license__'), # Choose your license, note the American spelling
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Framework :: Django',
        'Topic :: Internet',
        'Topic :: Terminals',
        'Topic :: Security',
        'Topic :: Communications :: Email',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
    
    # used when people are searching for a module, keywords separated with a space
    keywords = 'dipense',
    include_package_data = True, # include files listed in MANIFEST.in
    
    # The list of packages(directories) for your library
    packages=find_packages(), # OR packages=['dipense'] 
    # If your package is a single module, use this instead of 'packages':
    # py_modules=[''] # list of files (modules) that are not in any directory (at the root dir)
    # the libraries it depends on
    
    # List of other python modules which this module depends on.  For example RPi.GPIO
    install_requires = [
        'folium>=0.13.0',
        'phonenumbers>=8.13.0',
        'geocoder>=1.38.1',
        'python-whois>=0.8.0',
        'termcolor>=2.1.0',
    ],
    project_urls={
        'Documentation': grep('__url__'),
        'Source': grep('__repository__'),
    },
)
