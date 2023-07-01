from rest_framework import serializers

from apps.posts.models import Post, PostLike, PostComment


class PostLikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = "__all__"

class PostCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostComment
        fields = "__all__"

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = "__all__"