from django.contrib import admin
from .models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cat_id','title','url','image', 'date']

class PostAdmin(admin.ModelAdmin):
    list_display = ['post_id','title','url','cat','image']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)