from graphene import relay, ObjectType, Schema
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from temple.models import Level, Student, Volunteer, Class
from django.contrib.auth.mixins import LoginRequiredMixin
from graphene_django.views import GraphQLView
"""
GraphQL

"""
class LevelNode(DjangoObjectType):
    class Meta:
        model=Level
        only_fields=('name')
        filter_fields = ['name']
        interfaces = (relay.Node, )
class StudentNode(DjangoObjectType):
    class Meta:
        model=Student
        only_fields=('name', 'created', 'class_level', 'added_by', 'volunteer')
        filter_fields = {
        'name': ['exact', 'icontains', 'istartswith'],
        }
        interfaces = (relay.Node, )
class VolunteerNode(DjangoObjectType):
    class Meta:
        model=Volunteer
        only_fields=('sector_name')
        filter_fields=['sector_name']
        interfaces = (relay.Node,)
class ClassNode(DjangoObjectType):
    class Meta:
        model=Class
        only_fields=('name', 'level', 'start_date', 'end_date')
        filter_fields=['name', 'level']
        interfaces = (relay.Node,)
class Query(ObjectType):
    all_levels = DjangoFilterConnectionField(LevelNode)
    all_students = DjangoFilterConnectionField(StudentNode)
    all_volunteers = DjangoFilterConnectionField(VolunteerNode)
    all_classes = DjangoFilterConnectionField(ClassNode)

class PrivateGraphQLView(LoginRequiredMixin, GraphQLView):
    pass
write_schema = Schema(query=Query, mutation=Mutation)
read_schema = Schema(query=Query)

schema = Schema(query=Query)
