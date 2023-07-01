from rest_framework.routers import DefaultRouter

from apps.posts.views import PostAPIViewSet, PostLikeAPIViewSet, PostCommentAPIViewSet


router = DefaultRouter()
router.register('posts', PostAPIViewSet, "api_posts")
router.register('likes', PostLikeAPIViewSet, "api_likes")
router.register('comments', PostCommentAPIViewSet, "api_comments")

urlpatterns = router.urls