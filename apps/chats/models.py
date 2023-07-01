from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Chat(models.Model):
    from_user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        related_name='chat_from_user',
        null=True
    )
    to_user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        related_name='chat_to_user',
        null=True
    )

    def __str__(self):
        return f"{self.from_user} {self.to_user}"
    
    class Meta:
        verbose_name = 'Чат'
        verbose_name_plural = 'Чаты'
        unique_together = ('from_user', 'to_user')

class Message(models.Model):
    chat = models.ForeignKey(
        Chat, on_delete=models.CASCADE,
        related_name='chat_messages'
    )
    sender = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        related_name='sender_messages',
        null=True
    )
    text = models.CharField(
        max_length=350,
        verbose_name='Текст'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания"
    )

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'