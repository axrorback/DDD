from django.contrib import admin
from apps.users.infrastructure.models import UserModel

@admin.register(UserModel)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("email",)
