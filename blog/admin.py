from django.contrib import admin

# Register your models here.
# from blog.models import Publication, Post, Category
from blog.models import Profile, Class, Volunteer, Student, Class_Material
#
# @admin.register(Publication)
# class PublicationAdmin(admin.ModelAdmin):
#   list_display = ('name', 'slug')
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#   list_display = ('title', 'slug', 'created', 'blog')
#   list_filter = ('created',) # add a filter box with one command!!! wtfff
#   search_fields = ('title', 'slug', 'body') #allows you to add a search field
# @admin.register(Category)
# class CategoryAdmin(admin.ModelAdmin):
#     list_display=('name', )
#     search_fields = ('name',)
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display=('name','level', 'start_date', 'end_date' )
@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display=('sector_name', 'user')
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display=('user', 'email_confirmed')
    list_filter = ('user',)
    search_fields = ['user__username', 'user__first_name', 'user__last_name', 'user__email']
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display=('user', 'class_level','created')
    list_filter = ('class_level__level',)
@admin.register(Class_Material)
class Class_MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'upload', 'class_level')
