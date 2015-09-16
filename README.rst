=============
rucola-drafts
=============

A Rucola plugin used to ignore draft pages.

Installation
------------

You can install using ``pip``: ::

    pip install rucola-drafts

Usage
-----

Plugin will ignore each file that ``draft`` metadata is ``True``:

An example project directory::

    src/
        index.html
        not-ready.html
    script.py

Content of ``script.py``:

.. code-block:: python

    from rucola import Rucola
    from rucola_drafts import Drafts

    app = Rucola('.')
    file = app.get('not-ready.html')
    file['draft'] = True

    app.use(
        Drafts()
    )
    app.build()

As a result, page ``not-ready.html`` is not build: ::

    build/
        index.html


Using with other plugins
~~~~~~~~~~~~~~~~~~~~~~~~

It is good to use ``Drafts`` with
`YamlContext <https://github.com/lecnim/rucola-yamlfm/>`_ plugin. If you do that,
you can set a page to a draft mode using just the YAML frontmatter:

.. code-block:: markdown

    """
    draft: true
    """

    I am working on it blab bla bla...


License
-------

MIT