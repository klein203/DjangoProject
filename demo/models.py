import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _


class Record(models.Model):
    name = models.CharField(_('Record.Name'), max_length=50, null=False, blank=False)
    age = models.IntegerField(_('Record.Age'), null=True, blank=True)
    gender = models.CharField(_('Record.Gender'), max_length=1, null=True, blank=True, choices=(
        ('M', _('DICT.GENDER.Male')),
        ('F', _('DICT.GENDER.Female')),
    ))
    date_of_birth = models.DateField(_('Record.DateOfBirth'), null=False, blank=False, default=datetime.datetime(1981, 1, 1))
    create_time = models.DateTimeField(_('Record.CreateTime'), auto_now_add=True)
    update_time = models.DateTimeField(_('Record.UpdateTime'), auto_now=True)

    class Meta:
        verbose_name = _('Record')
        verbose_name_plural = _('Records')

    def __str__(self):
        return self.name
