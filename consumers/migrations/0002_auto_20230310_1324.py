# Generated by Django 3.2.13 on 2023-03-10 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consumers', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='consumers',
            options={'verbose_name': 'مصرف کننده', 'verbose_name_plural': 'مصرف کنندگان'},
        ),
        migrations.AlterField(
            model_name='consumers',
            name='family',
            field=models.CharField(max_length=150, verbose_name='نام خانوادگی'),
        ),
        migrations.AlterField(
            model_name='consumers',
            name='name',
            field=models.CharField(max_length=150, verbose_name='نام'),
        ),
        migrations.AlterField(
            model_name='consumers',
            name='number_of_members',
            field=models.IntegerField(verbose_name='تعداد اعضای خانواه'),
        ),
    ]