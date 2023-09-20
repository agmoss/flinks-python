import codecs
from os.path import abspath
from os.path import dirname
from os.path import join
from setuptools import find_packages
from setuptools import setup

import pyflinks


def read_relative_file(filename):
    """ Returns contents of the given file, whose path is supposed relative to this module. """
    with codecs.open(join(dirname(abspath(__file__)), filename), encoding='utf-8') as f:
        return f.read()


setup(
    name='pyflinks',
    version=pyflinks.__version__,
    author='Andrew Moss',
    author_email='andrew@m0ss.dev',
    packages=find_packages(exclude=['tests.*', 'tests']),
    package_data={"pyflinks": ["py.typed"]},
    include_package_data=True,
    url='https://github.com/agmoss/python-flinks',
    license='MIT',
    description='A Python module for communicating with the Flinks.io API.',
    long_description=read_relative_file('README.rst'),
    keywords='flinks bank financial data institution',
    zip_safe=False,
    install_requires=[
        'requests>=2.0',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
    ],
)
