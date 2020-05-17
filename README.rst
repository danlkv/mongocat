========
mongocat
========


.. image:: https://img.shields.io/pypi/v/mongocat.svg
        :target: https://pypi.python.org/pypi/mongocat

.. image:: https://img.shields.io/travis/DaniloZZZ/mongocat.svg
        :target: https://travis-ci.com/DaniloZZZ/mongocat

.. image:: https://readthedocs.org/projects/mongocat/badge/?version=latest
        :target: https://mongocat.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status


.. image:: https://pyup.io/repos/github/DaniloZZZ/mongocat/shield.svg
     :target: https://pyup.io/repos/github/DaniloZZZ/mongocat/
     :alt: Updates



Cli tool to interact with mongodb


* Free software: MIT license
* Documentation: https://mongocat.readthedocs.io.

Overview
--------

Write new documents into collection.

.. code-block:: bash

    $ export MONGOCAT_URL='mongodb://<username>:<password>@your-mongo-host'
    $ mongocat -W -d tensim graphs
    foo: bar                                # enter your object in minified yaml
    5ec0a27324ec53bd2464c074                # prints object id on success
    foo: baz
    5ec0a27a24ec53bd2464c075

Read documents from a collection

.. code-block:: bash

    $ mongocat -R -d tensim graphs
    {'_id': ObjectId('5ec0a27324ec53bd2464c074'), 'foo': 'bar'}
    {'_id': ObjectId('5ec0a27a24ec53bd2464c075'), 'foo': 'baz'}


Usage
-----

.. code-block:: bash

    $ mongocat --help
    Usage: mongocat [OPTIONS] COLLECTION

      Read/write to mongodb COLLECTION.

    Options:
      -R, --read
      -W, --write
      -p, --parser [json|yaml]
      -u, --url TEXT            MongoDB URI. format:
                                mongodb://[username:password@]host1[:port1]...

      -d, --database TEXT       Database name
      --help                    Show this message and exit.

Combine with the power of unix
------------------------------

Dump running processes to db

.. code-block:: bash

	$ ps | jc --ps | jq -cM '.[]' | mongocat -WR -d tensim processes
	5ec0aeef4814de15eb742155
	5ec0aeef4814de15eb742156
	5ec0aeef4814de15eb742157
	5ec0aeef4814de15eb742158
	5ec0aeef4814de15eb742159
	{'_id': ObjectId('5ec0aeef4814de15eb742155'), 'pid': 195657, 'tty': 'pts/8', 'time': '00:01:05', 'cmd': 'fish'}
	{'_id': ObjectId('5ec0aeef4814de15eb742156'), 'pid': 396223, 'tty': 'pts/8', 'time': '00:00:00', 'cmd': 'ps'}
	{'_id': ObjectId('5ec0aeef4814de15eb742157'), 'pid': 396224, 'tty': 'pts/8', 'time': '00:00:00', 'cmd': 'jc'}
	{'_id': ObjectId('5ec0aeef4814de15eb742158'), 'pid': 396225, 'tty': 'pts/8', 'time': '00:00:00', 'cmd': 'jq'}
	{'_id': ObjectId('5ec0aeef4814de15eb742159'), 'pid': 396226, 'tty': 'pts/8', 'time': '00:00:00', 'cmd': 'mongocat'}

Curl straight into DB

.. code-block:: bash

	$ curl 'https://api.github.com/repos/DaniloZZZ/mongocat/commits?per_page=5' |\
	 jq -cM '.[] | {msg: .commit.message, name: .commit.committer.name}' |\
	 mongocat -WR -d tensim commits
	  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
									 Dload  Upload   Total   Spent    Left  Speed
	100 11145  100 11145    0     0  47628      0 --:--:-- --:--:-- --:--:-- 47628
	5ec0aa4ac6ddf6dc2bf2def9
	5ec0aa4ac6ddf6dc2bf2defa
	5ec0aa4ac6ddf6dc2bf2defb
	{'_id': ObjectId('5ec0aa4ac6ddf6dc2bf2def9'), 'msg': 'First working version', 'name': 'Danil Lykov'}
	{'_id': ObjectId('5ec0aa4ac6ddf6dc2bf2defa'), 'msg': 'upd deps', 'name': 'Danil Lykov'}
	{'_id': ObjectId('5ec0aa4ac6ddf6dc2bf2defb'), 'msg': 'init', 'name': 'Danil Lykov'}

Tools used:
	- `jc`: https://github.com/kellyjonbrazil/jc
	- `jq`: https://github.com/stedolan/jq


TODO
----

- [ ] Option to suppress print of added document
- [ ] Finding command that filters documents aka mongo grep
- [ ] Deleting documens using ids from stdin. Delete some: ``mongocat --find 'blah' | mongocat --delete``

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
