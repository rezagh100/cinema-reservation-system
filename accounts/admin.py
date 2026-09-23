from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ("Personal Info", {"fields": ("phone_number",)}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        ("Personal Info", {"fields": ("phone_number",)}),
    )
