from django.contrib import admin
from homepage.models import Index

# Register your models here.
class IndexAdmin(admin.ModelAdmin):
    list_display = ['my_name', 'my_email', 'my_description', 'languages_learnt']
    ordering = ['my_name']

admin.site.register(Index, IndexAdmin)