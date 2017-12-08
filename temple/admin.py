from django.contrib import admin
from temple.models import Level, Student, Class, Volunteer, Class_Material# Register your models here.
"""
SuperUser Account Login:

username: julie
password: julianamei

"""
@admin.register(Level)
class LevelAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ('sector_name',)

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('name','level', 'start_date', 'end_date')
    list_filter = ('level', 'start_date')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'class_level', 'created','added_by', 'volunteer')
    search_fields = ['name','class_level__name', 'volunteer__sector_name']

@admin.register(Class_Material)
class Class_MaterialAdmin(admin.ModelAdmin):
    list_display = ('id', 'upload')
