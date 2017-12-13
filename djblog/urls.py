"""djblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from djzen.urls import zen_url
from graphene_django.views import GraphQLView
from django.views.decorators.csrf import csrf_exempt
from blog.schema import read_schema, write_schema, PrivateGraphQLView
import blog.views
import temple.views

#Django-material front-end starter templates
from material.frontend import urls as frontend_urls

urlpatterns = [
    zen_url('admin/', admin.site.urls),
    zen_url('', include(frontend_urls)),
    zen_url('', blog.views.index, name='home'),
    zen_url('masters/', blog.views.masters),
    zen_url('meditate/', blog.views.meditate, name='meditate'),
    zen_url('myclasses/meditate/<slug>/material', blog.views.meditate_classes_material),
    zen_url('meditate/<slug>/signup', blog.views.meditate_classes_signup),
    zen_url('myclasses/', blog.views.my_classes, name='myclasses'),
    zen_url('about/', blog.views.about),
    zen_url('profile/', blog.views.ProfileView.as_view(), name='profile'),
    # zen_url('volunteer/', blog.views.VolunteerView.as_view(), name='volunteer'),
    zen_url('volunteer/', blog.views.volunteer, name='volunteer'),
    zen_url('volunteer/<slug>/', blog.views.volunteer_signup),
    zen_url('success/', blog.views.success, name='success'),
    zen_url('your-server-side-code/', blog.views.redirect_success),
    zen_url('donate/', blog.views.donate, name='donate'),
    zen_url('payments/', include('djstripe.urls', namespace="djstripe")),
    zen_url('teachings/<slug>/', blog.views.teachings),
    zen_url('accounts/', include('django.contrib.auth.urls')),
    zen_url('signup/', blog.views.signup, name='signup'),
    zen_url('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    zen_url('posts/<slug>/', blog.views.post_list),
    # zen_url('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
    zen_url('graphql-authed/', csrf_exempt(PrivateGraphQLView.as_view(graphiql=True, schema=write_schema))),
    zen_url('graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=read_schema))),
    zen_url('account_activation_sent/', blog.views.account_activation_sent, name='account_activation_sent'),
    zen_url('activate/<str:uidb64>/<str:token>', blog.views.activate, name="activate"),
    zen_url('home/', temple.views.temple_index),
    zen_url('contact/', blog.views.contact, name='contact'),
    zen_url('sandbox/', blog.views.sandbox),
    # zen_url('classes/', temple.views.classes),
    # zen_url('classes/all/', temple.views.ClassListView.as_view(), name='class'),
    # zen_url('classes/all/<int>/', temple.views.class_detail_view),
]
