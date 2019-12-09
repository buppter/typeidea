from django.db import models
from django.contrib.auth.models import User

from blog.models import Post
from config.models import Status


class Comment(models.Model):
    content = models.CharField(max_length=2000, verbose_name="内容")
    nickname = models.CharField(max_length=50, verbose_name="昵称")
    website = models.URLField(verbose_name="网站")
    email = models.EmailField(verbose_name="邮箱")
    target = models.CharField(max_length=100, verbose_name="评论目标")
    status = models.PositiveIntegerField(default=Status.STATUS_NORMAL, choices=Status.STATUS_ITEMS, verbose_name="状态")
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    @classmethod
    def get_by_target(cls, target):
        return cls.objects.filter(target=target, status=Status.STATUS_NORMAL)

    class Meta:
        verbose_name = verbose_name_plural = "评论"
