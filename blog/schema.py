from graphene import relay, ObjectType, Schema
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from blog.models import Publication, Post
from graphene_django.rest_framework.mutation \
    import SerializerMutation
from blog.serializer import PostSerializer, PubSerializer #for graphql mutation. serializers translate data into json
from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django.views import GraphQLView
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
class Mutation (ObjectType):
    add_post = AddPost.Field()
    add_pub = AddPub.Field()
class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass
write_schema = Schema(query=Query, mutation=Mutation)
read_schema = Schema(query=Query)
# schema = Schema(query=Query)
