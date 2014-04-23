from django.contrib import admin
from mezzanine.core.admin import OwnableAdmin
from mptt.admin import MPTTModelAdmin

from .models import Dump, DumpCategory


class DumpAdmin(admin.ModelAdmin):
    """Admin class for Dumps."""

    list_display = ("title", "description", "views", "category", "link",
                    "user")
    list_filter = ("user", "category")
    search_fields = ("title", "description", "category__title")
    fields = ("title", "link", "description", "category")
    date_hierarchy = "created"

    def save_form(self, request, form, change):
        """
        Set the object's owner as the logged in user.
        """
        obj = form.save(commit=False)
        if obj.user_id is None:
            obj.user = request.user
        return super(DumpAdmin, self).save_form(request, form, change)


class DumpCategoryAdmin(MPTTModelAdmin):
    """Admin class for Dump Categories."""
    list_display = ("title",)
    mptt_level_indent = 20


admin.site.register(Dump, DumpAdmin)
admin.site.register(DumpCategory, DumpCategoryAdmin)
