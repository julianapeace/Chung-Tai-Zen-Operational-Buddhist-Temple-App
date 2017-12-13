from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView #for VolunteerForm Class
# from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Post, Profile, Student, Class, Volunteer
from blog.serializer import PostSerializer
from blog.forms import SignUpForm, MailForm, BeginnerClassForm, VolunteerForm, ProfileForm
from blog.tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

from django.conf import settings #for stripe secret
import stripe
from django.core.mail import send_mail

@api_view(['GET']) #you can also include POST requests
def post_list (request, slug):
    posts = Post.objects.filter(blog__slug=slug) #look up posts by the FK Publication slug. Double underscore is doing a join.
    serializer = PostSerializer(posts, many=True) #pass the data to the serializer
    return Response(serializer.data) #send back the response

def index(request):
    import random
    import os
    quote_file = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'quotes.txt')
    f = open(quote_file, 'r', encoding='ISO-8859-1')
    """
    txt = f.read()
    lines = txt.split('\n.\n')
    """
    quote = random.choice(f.read().split('\n.\n'))
    return render(request, 'index.html', context={'quote':quote, 'width':1000, 'height':600, 'bgcolor':'FFFFFF','color':'000000'})
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            #################
            # Email confirmation sign up
            #################
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Activate Your Account'
            message = render_to_string('account_activation_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            user.email_user(subject, message)
            return redirect('account_activation_sent')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

def account_activation_sent(request):
    return render(request, 'account_activation_sent.html', context={})

def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('home')
    else:
        return render(request, 'account_activation_invalid.html')

def contact(request):
    # email='kmeinhardt7@gmail.com'
    # send_mail('chance is the subject', 'is the body of the message', 'noreply@chungtaizen.com', [email], fail_silently=False,)
    # print ('email sent to: ', email)
    form = MailForm()
    return render(request, 'contact.html',{'form': form})
def masters(request):
    return render(request, 'masters.html')
def validateStudent(level, theID):
    print('validateStudent: level:',level, 'ID:',theID)
    return Student.objects.filter(class_level__level=level, user__user=theID).count()
def meditate(request):
    if request.user.is_authenticated():
        theID = request.user.id
        levels = ['beginner', 'intermediate','advanced', 'children']
        classauth = []
        for i in levels:
            classauth.append(validateStudent(i,theID))
        print(classauth)
    else:
        classauth=[0,0,0,0]
    return render(request, 'meditate/meditate.html', {'classauth':classauth})

def createStudent(level, theID):
    level = Class.objects.get(level=level)#gets the latest class of matching level
    student = Profile.objects.get(user=theID)
    return Student.objects.create(class_level=level, user=student)

@login_required
def meditate_classes_signup(request,slug):
    if slug == 'beginner' or slug == 'intermediate' or slug == 'advanced' or slug=="children":
        if request.user.is_authenticated():
            theID = request.user.id
            createStudent(slug,theID)
            print('student is added to: ',slug)
        return redirect('meditate')

@login_required
def my_classes(request):
    if request.user.is_authenticated():
        theID = request.user.id
    q = Student.objects.filter(user__user=theID) #returns an array of student objects matching ID
    #get class name
    classes = []
    for i in q:
        classes.append([i.class_level, i.class_level.level])
    print(classes)

    q = Volunteer.objects.filter(user__user=theID)
    volunteer = []
    for i in q:
        volunteer.append([i.sector_name])
    print(volunteer)
    return render(request, 'myclasses.html', {'classes':classes, 'volunteer': volunteer})

@login_required
def meditate_classes_material(request, slug):
    if slug == 'beginner':
        form = BeginnerClassForm()
        return render(request, 'meditate/beginners.html')
    elif slug == 'intermediate':
        return render(request, 'meditate/intermediate.html')
    elif slug == 'advanced':
        return render(request, 'meditate/advanced.html')
    elif slug == 'children':
        return render(request, 'meditate/children.html')

class VolunteerView(CreateView):
    model = Volunteer
    form_class = VolunteerForm
    template_name = 'volunteer.html'
    success_url = '/success'
    # success_url = '/myclasses'

class ProfileView(CreateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profile.html'
def success(request):
    return render(request, 'success.html')
def redirect_success(request):
    return redirect ('success')
def sandbox(request):
    return render(request, 'sandbox.html')
def teachings(request, slug):
    return render(request, f'teachings/{slug}.html')

stripe.api_key = settings.STRIPE_LIVE_SECRET_KEY
def donate(request):
    return render(request, 'donate.html')
def about(request):
    return render(request, 'about.html')
