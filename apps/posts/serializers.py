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
    
class PostDetailSerializer(serializers.ModelSerializer):
    post_comments = PostCommentSerializer(read_only=True, many=True)
    comments_count = serializers.SerializerMethodField(read_only=True)
    
    posts_likes = PostLikeSerializer(read_only=True, many=True)
    likes_count = serializers.SerializerMethodField(read_only=True)
    
    class Meta:
        model = Post
        fields = ('id', 'title', 'description',
                  'image', 'created', 'user',
                  'post_comments', 'posts_likes',
                  'comments_count', 'likes_count')
    
    def get_comments_count(self, obj):
        return obj.post_comments.all().count()
    
    def get_likes_count(self, obj):
        return obj.posts_likes.all().count()