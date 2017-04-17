from django.conf import settings
from django.db import models

# Create your models here.

class Post(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL , related_name="+")
    # user.post_set.all() 충돌을 피하기 위함 '+'는 skip
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
