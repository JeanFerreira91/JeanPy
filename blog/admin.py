from django.contrib import admin
from blog.models import Post, Category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'created_on', 'last_modified']
    ordering = ['title']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    ordering = ['name']

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site_header = 'JeanPy Portfolio Admin'
admin.site.site_title = 'JeanPy Admin'
admin.site.index_title = 'Django Admin for JeanPy website'