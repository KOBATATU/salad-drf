from django.db import models

from user.models import User
from utils.models.baseModel import BaseModel

class Profile(BaseModel):
    class Meta:
        db_table='profile'
    #related_nameがあることでuser objectからprofileを参照できる
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    nickname=models.CharField(max_length=64,verbose_name="ニックネーム",null=False, blank=False)
    bio=models.TextField(max_length=1000, verbose_name="自己紹介", null=True, blank=True)
    avatar = models.ImageField(upload_to='static/',verbose_name="avatar", default="https://avatars.githubusercontent.com/u/44887498?v=4", null=True, blank=False)

    def __str__(self):
        return self.nickname or self.user.username

