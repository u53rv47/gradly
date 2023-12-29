"""
Django admin customization.
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from core import models


admin.site.register(models.Tag)
admin.site.register(models.Domain)
admin.site.register(models.Community)

admin.site.register(models.AIModel)


class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""

    ordering = ["id"]
    list_display = ["email", "first_name", "country"]
    fieldsets = (
        (
            None,
            {"fields": ("email", "password")},
        ),
        (
            _("Personal Info"),
            {"fields": ("first_name", "last_name", "dob", "gender", "country")},
        ),
        (
            _("Professional Info"),
            {"fields": ("profession", "industry", "institute", "major")},
        ),
        (
            _("Permissions"),
            {"fields": ("is_active", "is_staff", "is_superuser")},
        ),
        (_("Important dates"), {"fields": ("last_login",)}),
    )
    readonly_fields = ["last_login"]
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": (
                    "email",
                    "password1",
                    "password2",
                    "first_name",
                    "last_name",
                    "username",
                    "dob",
                    "gender",
                    "country",
                    "is_verified",
                    "is_active",
                    "is_staff",
                    "is_superuser",
                ),
            },
        ),
    )


admin.site.register(models.Institute)
admin.site.register(models.Industry)
admin.site.register(models.Major)

admin.site.register(models.User, UserAdmin)

admin.site.register(models.Post)
admin.site.register(models.Comment)
admin.site.register(models.Like)
