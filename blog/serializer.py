from rest_framework import serializers
from blog.models import Post, Publication
class PostSerializer(serializers.ModelSerializer):
  author_id = serializers.IntegerField(required=True)
  blog_id = serializers.IntegerField(required=True)

#why did we add blogid and authorid? Because they're forignkeys
  class Meta:
    model = Post
    fields = ('title', 'slug', 'body', 'created', 'blog_id', 'author_id')
    # fields = '__all__'

  def create(self, validated_data):
    print(validated_data)
    return Post.objects.create(**validated_data)

class PubSerializer(serializers.ModelSerializer):
  class Meta:
    model = Publication
    fields = ('name', 'slug')

  def create(self, validated_data):
    print(validated_data)
    return Publication.objects.create(**validated_data)
