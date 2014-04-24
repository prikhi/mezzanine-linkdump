from django.conf.urls import patterns, url


urlpatterns = patterns("linkdump.views",
    url("^$", "link_dump_list", name="link_dump_list"),
    url("^category/(?P<category>.*)/$", "link_dump_list",
        name="link_dump_list"),
    url("^tags/(?P<keyword_slug>.*)/$", "link_dump_tag_list",
        name="link_dump_tag_list"),
    url("^(?P<dump_slug>.*)/$", "link_dump_redirect",
        name="link_dump_redirect"),
)
