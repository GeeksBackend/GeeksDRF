from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny

from apps.posts.models import Post, PostLike, PostComment
from apps.posts.serializers import PostSerializer, PostLikeSerializer, PostCommentSerializer
from apps.posts.permissions import PostPermission

# Create your views here.
class PostAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Post.objects.all() #Django ORM: SELECT * FROM posts_post;
    serializer_class = PostSerializer
    # permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (PostPermission(), )
        return (AllowAny(), )
    
class PostLikeAPIViewSet(GenericViewSet,
                         mixins.CreateModelMixin,
                         mixins.DestroyModelMixin):
    queryset = PostLike.objects.all()
    serializer_class = PostLikeSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (PostPermission(), )
        return (AllowAny(), )

class PostCommentAPIViewSet(GenericViewSet,
                            mixins.CreateModelMixin,
                            mixins.DestroyModelMixin):
    queryset = PostComment.objects.all()
    serializer_class = PostCommentSerializer

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
    
    def get_permissions(self):
        if self.action in ('update', 'partial_update', 'destroy'):
            return (PostPermission(), )
        return (AllowAny(), )