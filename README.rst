=========
LinkDump
=========

LinkDump is a Mezzanine module that lets you create, display and track links.

Example usage can be seen at `SleepAnarchy.com`_


Usage
======

Install the package and dependencies via pip::

    pip install mezzanine-linkdump

Add the ``linkdump`` app and the ``mptt`` dependency to your
``INSTALLED_APPS``::

    INSTALLED_APPS = (
        # ...

        "mptt",
        "linkdump",
    )

Include the urls into your project's ``urls.py``::

    urlpatterns += patterns('',
        ("^links/", include('linkdump.urls')),
        ("^", include("mezzanine.urls")),
    )

If you want a shorter link for the redirects, route the URL to the
``linkdump.views.link_dump_redirect`` view::

    urlpatterns += patterns('',
        ("^links/", include('linkdump.urls')),
        (r"^l/(.*)", "linkdump.views.link_dump_redirect"),
        ("^", include("mezzanine.urls")),
    )

To integrate into the navigation, create a new Page with ``links`` as the URL.


Config
=======

The following settings may be specified in your project's ``settings.py``:

* ``LINKDUMP_SLUG_CHOICES`` - Characters used for link slugs.
* ``LINKDUMP_SLUG_LENGTH`` - Length of generated slugs.


Contributing
=============

You can install prerequisites using ``pip``::

    pip install -r requirements.txt

The official bug tracker lives at
http://bugs.sleepanarchy.com/projects/mezzanine-linkdump/, but a github mirror
is available for pull requests at http://github.com/prikhi/mezzanine-linkdump/.

.. _SleepAnarchy.com:       http://sleepanarchy.com/links/
