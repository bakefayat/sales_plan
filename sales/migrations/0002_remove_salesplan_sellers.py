# Generated by Django 4.1.7 on 2023-03-15 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salesplan',
            name='sellers',
        ),
    ]
