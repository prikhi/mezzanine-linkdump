=========
LinkDump
=========

LinkDump is a Mezzanine module that lets you create, display and track links.


Usage
======

Install via pip::

    pip install mezzanine-linkdump

Add it to your ``INSTALLED_APPS``::

    INSTALLED_APPS = (
        # ...

        "linkdump",
    )

Include the urls into your project's ``urls.py``::

    urlpatterns += patterns('',
        ("^links/", include('linkdump.urls')),
        ("^", include("mezzanine.urls")),
    )

To make a navigation link, create a new Page with ``links`` as the URL.
