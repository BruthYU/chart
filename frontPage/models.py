from django.db import models

# Create your models here.
class User(models.Model):

    genders = (
        ('male', "男"),
        ('female', "女"),
    )
    kinds = (
        ('senior',"研究生"),
        ('junior',"本科生"),
        ('Teacher', "教师"),
    )
    num = models.CharField(max_length=12,unique=True)
    name = models.CharField(max_length=128)
    password = models.CharField(max_length=12)

    gender = models.CharField(max_length=32, choices=genders, default="男")
    kind = models.CharField(max_length=32, choices=kinds, default="研究生")
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"