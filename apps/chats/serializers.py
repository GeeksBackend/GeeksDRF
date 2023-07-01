from rest_framework import serializers

from apps.chats.models import Chat, Message


class ChatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Chat 
        fields = ('id', 'from_user', 'to_user')

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'chat', 'sender',
                  'text', 'created')
        
class ChatDetailSerializer(serializers.ModelSerializer):
    chat_messages = MessageSerializer(read_only=True, many=True)
    
    class Meta:
        model = Chat 
        fields = ('id', 'from_user', 'to_user', 'chat_messages')