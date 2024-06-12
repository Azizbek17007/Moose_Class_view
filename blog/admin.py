from django.contrib import admin
from .models import Comment, Tags, Author, About, Article


# from .models import *
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('id','title')
    list_display_links = ('id','title')
    search_fields = ['title']
    filter_horizontal = ['tags']


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author',)
    list_display_links = ('id', 'title', 'author',)
    filter_horizontal = ('tags',)
    list_filter = ('author',)
    search_fields = ('id', 'title', 'author')


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'occupation')
    list_display_links = ('id','name', 'occupation')
    filter_horizontal = ('social_media', )


admin.site.register(Author)
admin.site.register(Comment)
admin.site.register(Tags)
admin.site.register(Article, ArticleAdmin)
admin.site.register(About)
