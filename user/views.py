from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .serializers import UserSerializer, UserLoginSerializer, CustomRegisterSerializer, UsernameUniqueCheckSerializer, \
    EmailUniqueCheckSerializer
from rest_framework import generics, status


# 회원가입
@permission_classes([AllowAny])  # 누구나 접근 가능
class Registration(generics.GenericAPIView):
    serializer_class = CustomRegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)

        serializer.is_valid(raise_exception=True)
        user = serializer.save(request)
        return Response(
            {
                # get_serializer_context: serializer에 포함되어야 할 어떠한 정보의 context를 딕셔너리 형태로 리턴
                # 디폴트 정보 context는 request, view, format
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data
            },
            status=status.HTTP_201_CREATED,
        )


# 로그인
@permission_classes([AllowAny])
class Login(generics.GenericAPIView):
    serializer_class = UserLoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Request Body Error."}, status=status.HTTP_409_CONFLICT)

        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        if user['username'] == "None":
            return Response({"message": "fail"}, status=status.HTTP_401_UNAUTHORIZED)

        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": user['token']
            }
        )


# 유저네임 중복 확인
class UsernameUniqueCheck(generics.CreateAPIView):
    serializer_class = UsernameUniqueCheckSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            return Response(data={'detail': ['You can use this ID']}, status=status.HTTP_200_OK)

        else:
            detail = dict()
            detail['detail'] = serializer.errors['username']
            return Response(data=detail, status=status.HTTP_409_CONFLICT)


# 이메일 중복 확인
class EmailUniqueCheck(generics.CreateAPIView):
    serializer_class = EmailUniqueCheckSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data, context={'request': request})

        if serializer.is_valid():
            return Response(data={'detail': ['You can use this Email']}, status=status.HTTP_200_OK)

        else:
            detail = dict()
            detail['detail'] = serializer.errors['email']
            return Response(data=detail, status=status.HTTP_409_CONFLICT)
