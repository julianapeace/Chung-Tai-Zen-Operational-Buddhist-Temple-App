from django.db import models
from django.conf import settings #

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class Publication(models.Model):
  name = models.CharField(max_length=280) # just like peewee
  slug = models.SlugField(max_length=50, unique=True) #want each slug to be unique

  def __str__(self):
      return self.name #problem: in admin page, the publication shows up as publication object because it doesnt recognize it as a string. this method says when you try to convert this obj to string, use the name.
class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Post(models.Model):
  title = models.CharField(max_length=50)
  image = models.FileField(null=True, blank=True)
  subtitle = models.CharField(max_length=140,
                              blank=True, null=True)
  slug = models.SlugField(max_length=50, unique=True)
  body = models.TextField()
  created = models.DateTimeField(auto_now=False, auto_now_add=True)
  updated = models.DateTimeField(auto_now=True, auto_now_add=False)
  blog = models.ForeignKey(Publication) #have a fk that points to publications
  # categories = models.ForeignKey(Category)
  author = models.ForeignKey(settings.AUTH_USER_MODEL) #must import settings first. line 2. point to tht e authorized users model.
  def __str__(self):
      return self.title
  class Meta:
      ordering = ['-created', '-updated'] # you most likely want to see post ordered backwards. so you want to add the "-"
      # everytime you look at posts, it will always show in this order
class Comment(models.Model):
    name = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)
    karma = models.BooleanField()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)
    # other fields...
    def __str__(self):
        name = f'{self.user.last_name}, {self.user.first_name}'
        return name
    @receiver(post_save, sender=User)
    def update_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)
        instance.profile.save()

class Class(models.Model):
    CLASS_LEVELS = (
        ('beginner','beginner'),
        ('intermediate','intermediate'),
        ('advanced','advanced'),
        ('children','children'),
    )
    name = models.CharField(max_length=50, help_text="level + start date")
    level = models.CharField(max_length=30, choices = CLASS_LEVELS)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        # return self.level + self.start_date #to get 'Advanced11012016'
        return self.name
class Class_Material(models.Model):
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    class_level = models.ForeignKey(Class, null=False)

    def __str__(self):
        return self.upload.name

class Student(models.Model):
    class_level = models.ForeignKey(Class, null=False)
    user = models.ForeignKey(Profile, null=True)
    created = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.user} - Student Object'


class Volunteer(models.Model):
    SECTOR = (
        ('Acolyte', 'Acolyte'),
        ('Kitchen', 'Kitchen'),
        ('Dining Hall', 'Dining Hall'),
        ('Receptionist', 'Receptionist'),
        ('Tablets', 'Tablets'),
    )
    sector_name = models.CharField(max_length=50, choices = SECTOR)
    user = models.ForeignKey(Profile, null=True)

    def __str__(self):
        return self.sector_name
