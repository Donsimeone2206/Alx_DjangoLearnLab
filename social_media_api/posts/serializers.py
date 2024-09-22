from .models import Comment ,Post , Like
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):

    author = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Post
        fields = ['author','title','created_at','updated_at']
    def create(self , validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['author'] = user
        return Post.objects.create( **validated_data)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','user','content','created_at','updated_at']

    def create(self , validated_data):
        request = self.context.get('request')
        user = request.user
        validated_data['author'] = user
        return Comment.objects.create( **validated_data)

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['post', 'user']

   
