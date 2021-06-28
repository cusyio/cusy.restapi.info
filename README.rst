.. This README is meant for consumption by humans and pypi. Pypi can render rst files so please do not use Sphinx features.
   If you want to learn more about writing documentation, please check out: http://docs.plone.org/about/documentation_styleguide.html
   This text does not appear on pypi or github. It is a comment.

.. image:: https://github.com/cusyio/cusy.restapi.info/workflows/ci/badge.svg
    :target: https://github.com/cusyio/cusy.restapi.info/actions

.. image:: https://coveralls.io/repos/github/cusyio/cusy.restapi.info/badge.svg?branch=main
    :target: https://coveralls.io/github/cusyio/cusy.restapi.info?branch=main
    :alt: Coveralls

.. image:: https://img.shields.io/pypi/v/cusy.restapi.info.svg
    :target: https://pypi.python.org/pypi/cusy.restapi.info/
    :alt: Latest Version

.. image:: https://img.shields.io/pypi/status/cusy.restapi.info.svg
    :target: https://pypi.python.org/pypi/cusy.restapi.info
    :alt: Egg Status

.. image:: https://img.shields.io/pypi/pyversions/cusy.restapi.info.svg?style=plastic   :alt: Supported - Python Versions

.. image:: https://img.shields.io/pypi/l/cusy.restapi.info.svg
    :target: https://pypi.python.org/pypi/cusy.restapi.info/
    :alt: License


=================
cusy.restapi.info
=================

Provides endpoints for site and content information.


Features
--------

- Get information about the Plone site using the ``@siteinfo`` endpoint.
- Get information about a content item using the ``contentinfo`` endpoint.


Installation
------------

Install ``cusy.restapi.info`` by adding it to your buildout::

    [buildout]

    ...

    eggs =
        cusy.restapi.info


and then running ``bin/buildout``


Contribute
----------

- Issue Tracker: https://github.com/cusyio/cusy.restapi.info/issues
- Source Code: https://github.com/cusyio/cusy.restapi.info


Support
-------

If you are having issues, please let us know by adding a new ticket.


License
-------

The project is licensed under the GPLv2.
