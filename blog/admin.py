from django.contrib import admin

# Register your models here.
from blog.models import Publication, Post, Category
@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
  list_display = ('name', 'slug')
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
  list_display = ('title', 'slug', 'created', 'blog')
  list_filter = ('created',) # add a filter box with one command!!! wtfff
  search_fields = ('title', 'slug', 'body') #allows you to add a search field
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name', )
    search_fields = ('name',)
