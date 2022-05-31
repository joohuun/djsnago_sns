# user/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser  # 장고 기본 제공 유저모델
from django.conf import settings


# Create your models here.
class UserModel(AbstractUser):
    # DB 테이블의 이름을 지정
    class Meta:
        db_table = "my_user"

    bio = models.CharField(max_length=256, default='')
    follow = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='followee')
