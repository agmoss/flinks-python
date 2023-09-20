python-flinks
=============

.. image:: https://img.shields.io/pypi/l/python-flinks.svg
    :target: https://pypi.python.org/pypi/python-flinks/
    :alt: License

.. image:: https://img.shields.io/pypi/pyversions/python-flinks.svg
    :target: https://pypi.python.org/pypi/python-flinks

.. image:: https://img.shields.io/pypi/v/python-flinks.svg
    :target: https://pypi.python.org/pypi/python-flinks/
    :alt: Latest Version

.. image:: https://travis-ci.org/agmoss/python-flinks.svg?branch=master
    :target: https://travis-ci.org/agmoss/python-flinks

.. image:: https://codecov.io/gh/agmoss/python-flinks/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/agmoss/python-flinks

|

**python-flinks** is a Python module for communicating with the
`Flinks.io API <https://sandbox.flinks.io/documentation/>`_.

.. contents:: Table of Contents
    :local:

Main requirements
-----------------

Python_ 3.11+, Requests_ 2.0+.

Installation
------------

To install python-flinks, please use pip_ (or pipenv_) as follows:

.. code-block:: shell

    $ pip install --pre python-flinks

Basic usage
-----------

The first step to interact with the Flinks v3 API interface is to initialize a ``flinks.Client``
instance. You'll need a Flinks customer ID (and optionally a private API instance URL) to perform
this initialization:

.. code-block:: python

    >>> from python-flinks import Client
    >>> client = Client('<CUSTOMER_ID>', 'https://sandbox.flinks.io/v3/')

Then you can easily interact with the implemented entities and the underlying API endpoints. Here
are some examples:


.. code-block:: python

    >>> client.banking_services.authorize(login_id='<LOGIN_ID>', most_recent_cached=True)
    >>> client.banking_services.get_accounts_summary('<REQUEST_ID>')

Authors
-------

impak Finance <tech@impakfinance.com>.

License
-------

MIT. See ``LICENSE`` for more details.


.. _pip: https://github.com/pypa/pip
.. _pipenv: https://github.com/pypa/pipenv
.. _Python: https://www.python.org/
.. _Requests: http://docs.python-requests.org/en/master/
