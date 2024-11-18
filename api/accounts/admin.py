from django.contrib import admin

from accounts.models import User


@admin.register(User)
class AccountAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'date_joined', 'is_active']
    list_filter = ['username', 'is_active']
    search_fields = ['username']
