from django.test import TestCase
from django.contrib.auth import get_user_model
from blog.models import Publication, Post, Profile, Class, Student, Volunteer
from django.contrib.auth.models import User
# Create your tests here.

class BlogTestCase(TestCase):
    def setUp(self):
        User = get_user_model()
        self.author = User.objects.create(username="Narf")
        self.author.set_password('narf')
        self.author.save()

    def test_post(self):
        blog = Publication.objects.create(
                  name='Hello', slug='hw')
        post = Post.objects.create(
                  title = 'Test post', slug = 'test',
                  body = 'body', blog = blog,
                  author = self.author
        )
        self.assertEqual(blog.post_set.all().count(), 1)
    def test_temple(self):
        narf = User.objects.get(username="Narf")
        profile = Profile.objects.get(user=narf)
        class_level = Class.objects.create(level = 'advanced', name='advClass', start_date='2017-10-03', end_date='2017-10-03')
        student = Student.objects.create(class_level=class_level, user=profile)
        
