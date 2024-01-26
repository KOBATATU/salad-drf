import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    class Meta:
        db_table = 'user'
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(verbose_name='email', blank=False, null=False, unique=True)
    location = models.CharField(verbose_name="住居", max_length=50, blank=True, null=True)
    birth_date = models.DateField(verbose_name="誕生日", blank=True, null=True)
    is_private = models.BooleanField(default=False)

    REQUIRED_FIELDS = ["email"]