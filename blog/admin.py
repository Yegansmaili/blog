from django.contrib import admin

from blog.models import *


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'updated_at', 'status', ]
    # ordering = ('title',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    ordering = ('-updated_at',)
    list_display = ['name', 'content','post','created_at',]
# admin.site.register(Post, PostAdmin)
