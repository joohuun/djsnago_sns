# user/models.py
from django.db import models


# Create your models here.
class UserModel(models.Model):
    # DB 테이블의 이름을 지정
    class Meta:
        db_table = "my_user"

    username = models.CharField(max_length=20, null=False)
    password = models.CharField(max_length=256, null=False)
    bio = models.CharField(max_length=256, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
