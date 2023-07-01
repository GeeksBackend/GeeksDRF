from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated

from apps.chats.models import Chat, Message
from apps.chats.serializers import ChatSerializer, MessageSerializer, ChatDetailSerializer

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

class MessageAPIViewSet(GenericViewSet,
                        mixins.ListModelMixin,
                        mixins.RetrieveModelMixin,
                        mixins.CreateModelMixin,
                        mixins.UpdateModelMixin,
                        mixins.DestroyModelMixin):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer