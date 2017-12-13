from graphene import relay, ObjectType, Schema
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from django.contrib.auth.models import User
from blog.models import Publication, Post, Profile, Class, Volunteer, Student
from graphene_django.rest_framework.mutation \
    import SerializerMutation
from blog.serializer import PostSerializer, PubSerializer, UserSerializer #for graphql mutation. serializers translate data into json
from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django.views import GraphQLView
class UserNode(DjangoObjectType):
    #fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
    class Meta:
        model = User
        only_fields = ('username', 'first_name', 'last_name', 'email')
        filter_fields = {
        'username': ['exact'],
        'first_name':['exact'],
        'last_name':['exact'],
        }
        interfaces = (relay.Node, )
class ProfileNode(DjangoObjectType):
    class Meta:
        model = Profile
        only_fields = ('user')
        filter_fields = {
        'user': ['exact'],
        }
        interfaces = (relay.Node, )
class StudentNode(DjangoObjectType):
    class Meta:
        model = Student
        only_fields = ('user', 'class_level', 'created')
        filter_fields = ['user']
        interfaces = (relay.Node, )
class VolunteerNode(DjangoObjectType):
    class Meta:
        model = Volunteer
        only_fields = ('sector_name', 'user')
        filter_fields = {
        'sector_name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )
class PublicationNode(DjangoObjectType):
    class Meta:
        model = Publication
        only_fields = ('name', 'slug')
        # filter_fields = ['slug']
        filter_fields = {
        'name': ['exact', 'icontains','istartswith'],
        'slug':['icontains']}
        interfaces = (relay.Node, )
class PostNode(DjangoObjectType):
    class Meta:
        model = Post
        only_fields = ('title', 'subtitle', 'body', 'created')
        filter_fields = {
        'title': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node,)
class Query(ObjectType):
    all_pubs = DjangoFilterConnectionField(PublicationNode)
    all_posts = DjangoFilterConnectionField(PostNode)
    all_volunteers = DjangoFilterConnectionField(VolunteerNode)
    all_students = DjangoFilterConnectionField(StudentNode)
    all_profiles = DjangoFilterConnectionField(ProfileNode)
    all_users = DjangoFilterConnectionField(UserNode)

    def resolve_all_posts(self,info):
    #this method filters queries
        if not info.context.user.is_authenticated():
            return Post.objects.none()
        else:
            return Post.objects.filter(author=info.context.user)
class AddPost (SerializerMutation):
    #perform mutation needed
    class Meta:
        serializer_class = PostSerializer
class AddPub (SerializerMutation):
    class Meta:
        serializer_class = PubSerializer
class AddUser (SerializerMutation):
    class Meta:
        serializer_class = UserSerializer
        
class Mutation (ObjectType):
    add_post = AddPost.Field()
    add_pub = AddPub.Field()
    add_user = AddUser.Field()

class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass
write_schema = Schema(query=Query, mutation=Mutation)
read_schema = Schema(query=Query)
# schema = Schema(query=Query)
