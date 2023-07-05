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
        
    def validate(self, attrs):
        chat = Chat.objects.get(pk=self.initial_data['chat'])
        if attrs['sender'] != chat.from_user or attrs['sender'] != chat.to_user or attrs['sender'] == self.context['request'].user:
            raise serializers.ValidationError({'chat':'У вас нету доступа к данному чату'})
        return attrs

class ChatDetailSerializer(serializers.ModelSerializer):
    chat_messages = MessageSerializer(read_only=True, many=True)
    
    class Meta:
        model = Chat 
        fields = ('id', 'from_user', 'to_user', 'chat_messages')