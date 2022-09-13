from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import update_last_login
from rest_framework_jwt.settings import api_settings
from rest_auth.registration.serializers import RegisterSerializer

from .models import User
from rest_framework import serializers

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

User = get_user_model()


# 회원가입
class CustomRegisterSerializer(RegisterSerializer):
    nickname = serializers.CharField(required=False, max_length=50)
    introduction = serializers.CharField(required=False, max_length=200)
    profile_image = serializers.ImageField(required=False)

    def get_cleaned_data(self):
        data_dict = super().get_cleaned_data()  # username, password, email이 디폴트
        data_dict['nickname'] = self.validated_data.get('nickname', '')
        data_dict['introduction'] = self.validated_data.get('introduction', '')
        data_dict['profile_image'] = self.validated_data.get('profile_image', '')

        return data_dict


# 로그인
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)
    token = serializers.CharField(max_length=100, read_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password", None)

        user = authenticate(username=username, password=password)

        if user is None:
            return {'username': 'None'}
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)

        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given username and password does not exist'
            )
        return {
            'username': user.username,
            'token': jwt_token
        }


# 사용자 정보 추출
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'nickname', 'introduction', 'profile_image')
