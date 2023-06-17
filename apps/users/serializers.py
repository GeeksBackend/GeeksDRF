from rest_framework import serializers

from apps.users.models import User 
from apps.posts.serializers import PostSerializer


class UserSerializer(serializers.ModelSerializer):
    user_posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = User 
        fields = ('id', 'username', 'first_name',
                  'last_name', 'profile_image', 'user_posts')
        
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=100, write_only=True
    )
    password2 = serializers.CharField(
        max_length=100, write_only=True
    )
    class Meta:
        model = User 
        fields = ('username', 'first_name', 'last_name',
                  'email', 'profile_image', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password':'Пароли отличаются'})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            email=validated_data['email'],
            profile_image=validated_data['profile_image'],
        )
        user.set_password(validated_data['password2'])
        user.save()
        return user