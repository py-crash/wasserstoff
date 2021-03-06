Wasserstoff
===========
|BuildStatus| |PyPIversion| |codecov| 

.. |BuildStatus| image:: https://travis-ci.org/lk-geimfari/wasserstoff.svg
    :target: https://travis-ci.org/lk-geimfari/wasserstoff
.. |PyPIversion| image:: https://badge.fury.io/py/wasserstoff.svg
    :target: https://badge.fury.io/py/wasserstoff
.. |codecov| image:: https://codecov.io/gh/lk-geimfari/wasserstoff/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/lk-geimfari/wasserstoff

**Wasserstoff** - is a library that help you store your configurations
for applications in JSON, INI and text files. The configuration will be easily loaded
to the scope of configuration object. The library was written with the
use of tools from the standard Python library, and therefore, it does
not have any side dependencies.


Installation
~~~~~~~~~~~~

::

    ➜  ~ pip install wasserstoff

or (when the project has been cloned):

::

    ➜  make test
    ➜  make install

Usage
~~~~~

Content of ``dev.json``:

.. code:: json

    {
      "smtp server": [
        "smtp.yandex.ru",
        "smtp.gmail.com"
      ],
      "port": 456,
      "ssl": true,
      "secret_key": "SECRET_KEY_HERE"
    }

Content of ``test.json``:

.. code:: json

    {
      "ssl": false,
      "secret_key": "001110110100101100101010100010111010"
    }

Loading configurations from the file:

.. code:: python


    >>> from wasserstoff import (
    ...     Config,
    ...     Environment,
    ... )

    >>> env = Environment()

    >>> dev = Config(
    ...     filename='dev',
    ...     scope='dev',
    ...     ext='json',
    ... )

    >>> test = Config(
    ...     filename='test',
    ...     scope='test',
    ...     ext='txt',
    ... )

    >>> env.patch(dev, test)
    >>> env.commit()


Now you can access to your configurations:

.. code:: python

    >>> env.dev.SMTP_SERVER
    ['smtp.yandex.ru', 'smtp.gmail.com']

    >>> env.dev.SSL
    True

    >>> env.dev.PORT
    456

    >>> env.dev.SECRET_KEY
    'SECRET_KEY_HERE'

    >>> env.test.SSL
    False

    >>> env.test.SECRET_KEY
    '001110110100101100101010100010111010'

License
~~~~~~~

Wasserstoff is licensed under the MIT License. See LICENSE for more
information.

.. toctree::
   :maxdepth: 3
   :caption: Contents:

   wasserstoff



Indices and tables
~~~~~~~~~~~~~~~~~~

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
