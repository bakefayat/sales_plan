# Generated by Django 4.1.7 on 2023-03-29 05:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0003_alter_sells_is_valid_alter_sells_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sells',
            name='is_valid',
        ),
    ]