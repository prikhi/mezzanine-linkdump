from django.db.models import Count
from mezzanine import template

from ..models import Dump, DumpCategory


register = template.Library()


@register.as_tag
def linkdump_top_dumps(limit=5):
    """
    Put a list of the top Dumps used into the template context.

    Usage::

        {% linkdump_top_dumps 5 as top_dumps %}

    """
    top_dumps = Dump.objects.order_by('-views')
    return list(top_dumps[:limit])


@register.as_tag
def linkdump_top_categories(limit=5):
    """
    Put a list of the top DumpCategories used into the template context.

    Usage::

        {% linkdump_top_categories 5 as top_categories %}

    """
    top_lexers = DumpCategory.objects.annotate(
        count=Count('dumps')).order_by('-count')
    return list(top_lexers[:limit])

@register.as_tag
def linkdump_recent_dumps(limit=5):
    """
    Put a list of the top DumpCategories used into the template context.

    Usage::

        {% linkdump_recent_dumps 5 as recent_dumps %}

    """
    recent_dumps = Dump.objects.order_by('-created')
    return list(recent_dumps[:limit])
