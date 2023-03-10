# Generated by Django 3.2.13 on 2023-03-10 14:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consumers', '0002_auto_20230310_1324'),
        ('sales', '0002_auto_20230310_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sells',
            name='consumer',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='sell', to='consumers.consumers', verbose_name='مصرف کننده'),
        ),
    ]
