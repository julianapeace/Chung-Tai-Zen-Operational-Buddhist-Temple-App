from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
# Create your models here.
class Class_Material(models.Model):
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Level(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Volunteer(models.Model):
    sector_name = models.CharField(max_length=50)

    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('volunteer-detail', args=[str(self.sector_name)])

    def __str__(self):
        return self.sector_name

class Class(models.Model):
    name = models.CharField(max_length=50)
    level = models.ForeignKey(Level)
    start_date = models.DateField()
    end_date = models.DateField()

    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('class-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

class Student(models.Model):
    name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    class_level = models.ForeignKey(Class)
    added_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    volunteer = models.ForeignKey(Volunteer, null=True)

    def get_absolute_url(self):
         """
         Returns the url to access a particular instance of MyModelName.
         """
         return reverse('student-detail', args=[str(self.id)])

    def __str__(self):
        return self.name
