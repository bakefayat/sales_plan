# Generated by Django 3.2.13 on 2023-03-10 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0002_auto_20230310_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='salesplan',
            name='seller',
            field=models.ManyToManyField(related_name='seller', to='sales.Sellers', verbose_name='فروشنده'),
        ),
    ]
