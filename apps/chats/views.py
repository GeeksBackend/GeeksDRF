from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from apps.chats.models import Chat, Message
from apps.chats.serializers import ChatSerializer, MessageSerializer, ChatDetailSerializer
from apps.chats.permissions import ChatPermission

from rest_framework.permissions import IsAuthenticated

# Create your views here.
class ChatAPIViewSet(GenericViewSet,
                     mixins.ListModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer

    def get_serializer_class(self):
        if self.action in ('retrieve', ):
            return ChatDetailSerializer
        return ChatSerializer
    
    def get_permissions(self):
        if self.action in ('retrieve', 'update', 'partial_update', 'destroy'):
            return (ChatPermission(), )
        return (IsAuthenticated(), )

    def perform_create(self, serializer):
        return serializer.save(from_user=self.request.user)

class MessageAPIViewSet(GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = (IsAuthenticated, )

    def perform_create(self, serializer):
        return serializer.save(sender=self.request.user)