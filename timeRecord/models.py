from django.db import models

class User(models.Model):
    mobile = models.CharField(max_length=11)
    openId = models.CharField(max_length=32)
    nickName = models.CharField(max_length=32)
    registerTime = models.CharField(max_length=19)
    loginTime = models.CharField(max_length=19)
    createTime = models.CharField(max_length=19)
    unionId = models.CharField(max_length=32)
