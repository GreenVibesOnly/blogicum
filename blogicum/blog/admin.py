from django.contrib import admin

from .models import Category, Comment, Location, Post


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'is_published',
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('title',)
    list_filter = ('is_published',)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'author',
        'post',
        'created_at',
    )
    search_fields = (
        'text',
        'author',
        'post'
    )
    list_filter = (
        'text',
        'author',
        'post'
    )


class LocationAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'is_published',
    )
    list_editable = (
        'is_published',
    )
    search_fields = ('name',)
    list_filter = ('is_published',)


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'is_published',
        'pub_date',
        'category',
        'location',
    )
    list_editable = (
        'is_published',
        'pub_date',
        'category',
        'location',
    )
    search_fields = ('title',)
    list_filter = (
        'author',
        'is_published',
        'pub_date',
        'category',
        'location',
    )
    list_display_links = (
        'title',
        'author',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
