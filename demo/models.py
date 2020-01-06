import datetime
from django.db import models


# Create your models here.
class Record(models.Model):
    name = models.CharField('Name', max_length=50, null=False, blank=False)
    age = models.IntegerField('Age', null=True, blank=True)
    gender = models.CharField('Gender', max_length=1, null=True, blank=True, choices=(
        ('M', 'Male'),
        ('F', 'Female'),
    ))
    date_of_birth = models.DateField('DOB', null=False, blank=False, default=datetime.datetime(1981, 1, 1))
    create_time = models.DateTimeField('CreateTime', auto_now_add=True)
    update_time = models.DateTimeField('UpdateTime', auto_now=True)

    class Meta:
        verbose_name = 'Record'
        verbose_name_plural = 'Records'

    def __str__(self):
        return self.name
