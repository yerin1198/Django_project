from django.contrib.auth import get_user_model, authenticate
from django.contrib.auth.models import update_last_login

from rest_framework.validators import UniqueValidator
from rest_framework_jwt.settings import api_settings
from rest_auth.registration.serializers import RegisterSerializer

from .models import User
from rest_framework import serializers

from .validators import CustomASCIIUsernameValidator

# JWT 사용 설정
JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

# 기본 유저 모델 불러오기
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
        # get_cleaned_data 함수에 필요한 정보를 추가적으로 입력할 수 있도록 커스터마이징
        return data_dict


# 아이디 중복 검사
class UsernameUniqueCheckSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True, min_length=3, max_length=30,
                                     validators=[UniqueValidator(queryset=User.objects.all()),
                                                 CustomASCIIUsernameValidator])

    class Meta:
        model = User
        fields = ['username']


# 이메일 중복 검사
class EmailUniqueCheckSerializer(serializers.ModelSerializer):
    email = serializers.CharField(required=True,
                                  validators=[UniqueValidator(queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ['email']


# 로그인
class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100, write_only=True)
    token = serializers.CharField(max_length=100, read_only=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password", None)
        # 사용자 아이디와 비밀번호로 로그인 할 수 있도록 구현
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
            'token': jwt_token  # 토큰도 함께 반환
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'username', 'nickname', 'introduction', 'profile_image')
