from rest_framework.routers import DefaultRouter

from apps.chats.views import ChatAPIViewSet, MessageAPIViewSet


router = DefaultRouter()
router.register('chats', ChatAPIViewSet, 'api_chats')
router.register('message', MessageAPIViewSet, 'api_message')

urlpatterns = router.urls 