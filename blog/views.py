from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
# from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from blog.models import Post, Profile
from blog.serializer import PostSerializer
from blog.forms import SignUpForm, MailForm
from blog.tokens import account_activation_token
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string

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
def meditate(request):
    #check if user is in the class, if yes, change button to 'view class'
    #if no, button is 'sign up', triggers sign up modal
    return render(request, 'meditate/meditate.html')
def volunteer(request):
    return render(request, 'volunteer.html')
def sandbox(request):
    return render(request, 'sandbox.html')
def meditate_classes(request, slug):
    if slug == 'beginner':

        return render(request, 'meditate/beginners.html')
    elif slug == 'intermediate':
        return render(request, 'meditate/intermediate.html')
    elif slug == 'advanced':
        return render(request, 'meditate/advanced.html')
    elif slug == 'children':
        return render(request, 'meditate/children.html')
def donate(request):
    return render(request, 'donate.html')
