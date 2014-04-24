from mezzanine import template


register = template.Library()


@register.filter('int_to_tabs')
def int_to_tabs(integer):
    """Return 8 spaces per integer."""
    return integer * 8 * '&nbsp;'


@register.filter('mult')
def multiply(integer, multiplier):
    """Multiple two numbers."""
    return integer * multiplier
