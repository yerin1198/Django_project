from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    # 일반 유저 생성
    def create_user(self, email, name, password):
        if not email:
            raise ValueError('must have user email')
        if not name:
            raise ValueError('must have user nickname')
        if not password:
            raise ValueError('must have password')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
            password=password
        )
        user.save(using=self._db)
        return user

    # 관리자 유저 생성
    def create_superuser(self, email, name, password):
        user = self.create_user(
            email,
            name=name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=100, null=False, blank=False, unique=True)
    name = models.CharField(max_length=100, null=False, blank=False, unique=True)
    password = models.CharField(max_length=100, null=False, blank=False)

    # User model의 필수 field
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # 헬퍼 클래스 사용
    objects = UserManager()

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = ['email', 'name', 'password']  # 필수로 작성해야 하는 field

    def __str__(self):
        return self.name
