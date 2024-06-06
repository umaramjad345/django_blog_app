from django.contrib import admin
from .models import Category, Post
from django.contrib.auth.models import Group, User


# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['image_tag','cat_id','title','url', 'date']
    search_fields = ['cat_id','title']
    list_per_page= 5


class PostAdmin(admin.ModelAdmin):
    list_display = ['image_tag','post_id','title','url','cat']
    search_fields = ['post_id','title']
    list_per_page= 5
    list_filter= ['cat']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)

admin.site.unregister(Group)
# admin.site.unregister(User)