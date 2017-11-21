from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class UserProfile(AbstractUser):
    GENDER_CHOICES = (
        ('male', '男'),
        ('female', '女')
    )
    nike_name = models.CharField(max_length=50, verbose_name='昵称', default='')
    birthday = models.DateField(verbose_name='生日', null=True, blank=True)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='female')
    address = models.CharField(max_length=100, default='')
    mobile = models.CharField(max_length=11, blank=True, null=True)
    image = models.ImageField(upload_to='images/%Y/%m', default='images/default.png', max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerifyRecord(models.Model):
    SEND_TYPE = (
        ('register', '注册'),
        ('forget', '忘记密码')
    )
    code = models.CharField(max_length=60, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    confirmed = models.BooleanField(default=False, verbose_name='是否已确认')
    send_type = models.CharField(choices=SEND_TYPE, max_length=10, verbose_name='类型')
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{0}({1})'.format(self.code, self.email)


class Banner(models.Model):
    title = models.CharField(max_length=100, verbose_name='标题')
    image = models.ImageField(upload_to='banner/%Y/%m', max_length=100, verbose_name='轮播图')
    url = models.URLField(max_length=200, verbose_name='访问地址')
    index = models.IntegerField(default=100, verbose_name='顺序')
    add_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name