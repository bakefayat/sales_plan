# Generated by Django 3.2.13 on 2023-03-10 09:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Seller',
            new_name='Sellers',
        ),
        migrations.AlterModelOptions(
            name='sellers',
            options={'verbose_name': 'فروشنده', 'verbose_name_plural': 'فروشندگان'},
        ),
    ]
