# emodels.py

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

status = models.IntegerField(choices=STATUS, default=0)

class Post(models.Model):
    title = models.CharField(max_length=200)
    # 内容
    content = models.TextField()
    # 创建时间
    date_created = models.DateTimeField(auto_now_add=True)
    # 唯一标识
    slug = models.SlugField(max_length=200, unique=True)
    # 作者
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    # 状态
    status = models.IntegerField(choices=status, default=0)