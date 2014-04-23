import random

from django.conf import settings
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext_lazy as _
from mptt.managers import TreeManager
from mptt.models import MPTTModel, TreeForeignKey
from mezzanine.core.models import Slugged, TimeStamped, Ownable


class Dump(Slugged, TimeStamped, Ownable):
    """A Dump is a link to be shared with the world.

    .. attribute:: link

        The link of the Dump.

    .. attribute:: description

        A brief description about the Dump.

    .. attribute:: views

        The number of views this Dump has received.

    .. attribute:: category

        The :class:`DumpCategory` the Dump belongs to.

    """
    link = models.URLField(verbose_name="External URL")
    description = models.CharField(max_length=200, blank=True)
    views = models.IntegerField(default=0, editable=False)
    category = models.ForeignKey("DumpCategory", verbose_name=_("Category"),
                                 related_name="dumps")

    class Meta:
        verbose_name = _("Link")
        verbose_name_plural = _("Links")
        ordering = ("title",)

    def save(self, *args, **kwargs):
        """Randomly generate a slug if one is not entered."""
        if not self.slug:
            self.slug = _generate_random_slug()
        super(Dump, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """Return the redirecting URL."""
        return reverse("linkdump.views.link_dump_redirect",
                       kwargs={'dump_slug': self.slug})


class DumpCategory(MPTTModel, Slugged):
    """Categorizes :class:`Dumps <Dump>`.

    .. attribute:: parent

        The parent :class:`DumpCategory`, if any.

    .. attribute:: tree

        The ``TreeManager`` for the category tree.

    """
    parent = TreeForeignKey('self', null=True, blank=True, db_index=True)
    tree = TreeManager()

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    class MPTTMeta:
        order_insertion_by=['title']

    def get_absolute_url(self):
        """Return the redirecting URL."""
        return reverse("linkdump.views.link_dump_list",
                       kwargs={'category': self.slug})


def _generate_random_slug(length=None, alphabet=None):
    length = length or getattr(settings, 'LINKDUMP_SLUG_LENGTH', 4)
    alphabet = alphabet or getattr(
        settings, 'LINKDUMP_SLUG_CHOICES',
        'abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNOPQRSTUVWXYZ1234567890')
    slug = ''.join([random.choice(alphabet) for i in range(length)])

    # Check if this slug already exists, if not, return this new slug
    try:
        Dump.objects.get(slug=slug)
    except Dump.DoesNotExist:
        return slug

    # Otherwise create a new slug which is +1 character longer than the
    # regular one.
    return generate_random_slug(length=length + 1)
