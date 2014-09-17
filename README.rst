=========
LinkDump
=========

LinkDump is a Mezzanine module that lets you create, display and track links.


Prerequisites
=============

MPTT ``django-mptt`` will be installed by ``setup.py`` but it will need to be
added to ``INSTALLED_APPS`` (see Usage below) for the admin views.

Usage
======

Install via pip::

    pip install mezzanine-linkdump

Add it to your ``INSTALLED_APPS``::

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
