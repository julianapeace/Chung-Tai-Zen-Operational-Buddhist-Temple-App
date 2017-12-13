from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from blog.models import Post, Profile, Student, Class, Volunteer
from django.forms import ModelForm

class VolunteerForm(ModelForm):
      class Meta:
        model = Volunteer
        fields = ('sector_name',)

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )

class ProfileForm(forms.Form):
    dob = forms.DateField()
    address1 = forms.CharField(max_length=100)
    address2 = forms.CharField(max_length=100)
    telephone = forms.CharField(max_length=10)
    EDUCATION = (
        ('HS','High School'),
        ('BS','Bachelors'),
        ('MS','Masters'),
        ('PhD','Ph.D'),
    )
    education = forms.ChoiceField(choices = EDUCATION)
    school_attended = forms.CharField(max_length=50)
    area_of_study = forms.CharField(max_length=50)
    job_title = forms.CharField(max_length=50)
    employer = forms.CharField(max_length=50)
    health_status = forms.CharField(max_length=100, help_text='Please list all health concerns e.g., high blood pressure, diabetes,etc.')
    buddhism_experience = forms.CharField(max_length=300)

    VOLUNTEER = (
        ('Reception', 'Reception'),
        ('Secretarial/typing','Secretarial/typing'),
        ('Computer Related/Database','Computer Related/Database'),
        ('Web Design','Web Design'),
        ('Writing/Editing','Writing/Editing'),
        ('Layout/Design','Layout/Design'),
        ('Printing','Printing'),
        ('Translation','Translation'),
        ('Fundraising','Fundraising'),
        ('Law', 'Law'),
        ('Accounting','Accounting'),
        ('Photography', 'Photography'),
        ('Audio/Video','Audio/Video'),
        ('Art and Decoration','Art & Decoration'),
        ('Chanting/Liturgy/Acolyte', 'Chanting/Liturgy/Acolyte'),
        ('Landscaping', 'Landscaping'),
        ('Kitchen','Kitchen'),
        ('Medical/Nursing','Medical/Nursing'),
        ('Construction','Construction'),
        ('Home Repair','Home Repair'),
        ('Janitorial','Janitorial'),
        ('Painting','Painting'),
        ('Sewing','Sewing'),
        ('Hospice Care','Hospice Care')
    )
    volunteer_interest = forms.MultipleChoiceField(choices = VOLUNTEER, required=False)
    class Meta:
      model = Profile
      fields = ('user','dob','volunteer_interest')

class MailForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
#paused here at 10:51PM https://docs.djangoproject.com/en/2.0/topics/forms/under FIELD DATA section
class BeginnerClassForm(forms.Form):
    #how to make a radio button for preferred Monday/Wednday class
    lead = forms.CharField(max_length=300, help_text='How did you find out about this class? Name of Introducer')
    followup = forms.BooleanField(required=False)
"""
FIELDS:
forms.URLField()
forms.IntgerField()
DateField(initial=datetime.date.today) with import datetime of course
BooleanField() empty value is false
CharField() has max and min length, strip() always set to True, empty_value
ChoiceField() like a dropdown but you type, set the choices yourself like I did in class_levels
MultipleChoiceField()
emailField() has max and min lenth
FileField and
ImageField requires that Pillow is installed with support for the image formats

ARGUMENTS:
required=False
label='my label' Gets displayed in the front
initial = 'Your name' or 'http://' Lets me specify the initial value when rendering
error_messages = {'required':'Please enter your name'} lets you customize error messages
"""

#FOLLOWING TUTORIAL: https://www.youtube.com/watch?v=Pn2x3Z7FKZA
