github_changelog
================

|Version| |Downloads| |Status| |Coverage| |License|

Changelog generation based off of Github history.


Installation
------------

::

    pip install github_changelog


.. include:: contributing.rst


Development
-----------

1. Create a new virtual environment
2. Install development requirements from *dev-requirements.txt*
3. Run tests  ``nosetests``
4. `detox`_ is installed and will run the test suite across all supported python platforms
5. `python setup.py build_sphinx` will generate documentation into *build/sphinx/html*

TL;DR
+++++

::

    $ virtualenv env
    $ ./env/bin/pip install -qr dev-requirements.txt
    $ source env/bin/activate
    (env) $ nosetests
    (env) $ python setup.py build_sphinx
    (env) $ detox


.. include:: ../HISTORY.rst


License
-------

.. include:: ../LICENSE


.. _detox: https://testrun.org/tox/

.. |Version| image:: https://badge.fury.io/py/github_changelog.svg?
   :target: http://badge.fury.io/py/github_changelog

.. |Status| image:: https://travis-ci.org/djt5019/github_changelog.svg?branch=master
   :target: https://travis-ci.org/djt5019/github_changelog

.. |Coverage| image:: https://img.shields.io/coveralls/djt5019/github_changelog.svg?
   :target: https://coveralls.io/r/djt5019/github_changelog

.. |Downloads| image:: https://pypip.in/d/github_changelog/badge.svg?
   :target: https://pypi.python.org/pypi/github_changelog

.. |License| image:: https://pypip.in/license/github_changelog/badge.svg?
   :target: https://github_changelog.readthedocs.org
