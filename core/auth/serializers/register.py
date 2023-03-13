from rest_framework import serializers

from core.user.models import User
from core.user.serializers import UserSerializer


class RegisterSerializer(UserSerializer):
    """Сериализатор регистрации для запросов и создания пользователей"""
    # Убедитесь, что пароль имеет длину не менее 8 и не более 128 символов и не может быть прочитан пользователем.
    password = serializers.CharField(max_length=128, min_length=8, write_only=True, required=True)

    class Meta:
        model = User
        # Список всех полей, которые могут быть включены в запрос или ответ
        fields = ['id', 'email', 'username', 'first_name', 'last_name', 'password']

    def create(self, validated_data):
        # Используйте метод create_user, который мы написали ранее для UserManager, чтобы создать нового пользователя.
        return User.objects.create_user(**validated_data)
    