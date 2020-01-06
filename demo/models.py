import datetime
from django.db import models


# Create your models here.
class Simple(models.Model):
    name = models.CharField('姓名', max_length=50, null=False, blank=False)
    age = models.IntegerField('年龄', null=True, blank=True)
    gender = models.CharField('性别', max_length=1, null=True, blank=True, choices=(
        ('M', 'Male'),
        ('F', 'Female'),
    ))
    date_of_birth = models.DateField('日期', null=False, blank=False, default=datetime.datetime(1981, 1, 1))
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        verbose_name = '简单表格'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
