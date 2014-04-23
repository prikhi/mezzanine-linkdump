from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import Dump, DumpCategory


class DumpAdmin(admin.ModelAdmin):
    """Admin class for Dumps."""

    list_display = ("title", "description", "views", "category", "link",
                    "user")
    list_filter = ("user", "category")
    search_fields = ("title", "description", "category__title")
    date_hierarchy = "created"


class DumpCategoryAdmin(MPTTModelAdmin):
    """Admin class for Dump Categories."""
    list_display = ("title",)
    mptt_level_indent = 20


admin.site.register(Dump, DumpAdmin)
admin.site.register(DumpCategory, DumpCategoryAdmin)
