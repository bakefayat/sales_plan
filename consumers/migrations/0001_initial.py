# Generated by Django 4.1.7 on 2023-03-09 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consumers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('family', models.CharField(max_length=150)),
                ('number_of_members', models.IntegerField()),
            ],
        ),
    ]
