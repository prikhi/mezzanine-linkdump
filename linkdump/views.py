from django.http import HttpResponseRedirect
from django.db.models import F
from django.shortcuts import get_object_or_404
from mezzanine.utils.views import render

from .models import Dump, DumpCategory


def link_dump_list(request, category=None, template="linkdump/list.html"):
    """Display the list of links, optionally filtered by category."""
    if category is not None:
        categories = [get_object_or_404(DumpCategory, slug=category)]
    else:
        categories = DumpCategory.objects.all()
    context = {"categories": categories, "category": category}
    return render(request, template, context)


def link_dump_redirect(request, dump_slug):
    """Increment the Dumps ``views`` count and redirect to the URL or 404."""
    dump = get_object_or_404(Dump, slug=dump_slug)
    Dump.objects.filter(slug=dump_slug).update(views=F('views') + 1)
    return HttpResponseRedirect(dump.link)
