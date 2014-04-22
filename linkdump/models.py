from django.db import models
from mptt.managers import TreeManager
from mptt.models import MPTTModel, TreeForeignKey
from mezzanine.core.models import Slugged, TimeStamped, Ownable


class Dump(Slugged, TimeStamped, Ownable):
    """A Dump is a link to be shared with the world.

    .. attribute:: link

        The link of the Dump.

    .. attribute:: description

        A brief description about the Dump.

    .. attribute:: visits

        The number of visits this Dump has received.

    .. attribute:: categories

        :class:`DumpCategories <DumpCategory>` the Dump belongs to.

    """

    def save(self, *args, **kwargs):
        """Randomly generate a slug if one is not entered."""


class DumpCategory(Slugged, MPTTModel):
    """Categorizes :class:`Dumps <Dump>`.

    .. attribute:: parent

        The parent :class:`DumpCategory`, if any.

    .. attribute:: tree

        The ``TreeManager`` for the category tree.

    """

    tree = TreeManager()
