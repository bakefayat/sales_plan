from django.db import models

# Create your models here.


class Consumers(models.Model):
    class Meta:
        verbose_name = 'مصرف کننده'
        verbose_name_plural = 'مصرف کنندگان'

    name = models.CharField(max_length=150, verbose_name='نام')
    family = models.CharField(max_length=150, verbose_name='نام خانوادگی')
    number_of_members = models.IntegerField(verbose_name='تعداد اعضای خانواه')

    def __str__(self):
        return f'{self.name} {self.family}'
