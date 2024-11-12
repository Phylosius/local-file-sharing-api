from django.contrib import admin

from files.models import FileInfo


@admin.register(FileInfo)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'upload_date')
    list_filter = ['upload_date']
    search_fields = ['name']

