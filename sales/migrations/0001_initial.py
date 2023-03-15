# Generated by Django 4.1.7 on 2023-03-15 06:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('consumers', '0002_auto_20230310_1324'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='آخرین بروزرسانی')),
                ('title', models.CharField(max_length=255, verbose_name='نام طرح')),
                ('is_active', models.BooleanField(default=True, verbose_name='فعال بودن')),
                ('total_capacity', models.IntegerField(verbose_name='حداکثر ظرفیت طرح')),
                ('description', models.TextField(null=True, verbose_name='توضیحات طرح')),
            ],
            options={
                'verbose_name': 'طرح فروش',
                'verbose_name_plural': 'طرح های فروش',
            },
        ),
        migrations.CreateModel(
            name='Sellers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('store_name', models.CharField(max_length=255, verbose_name='نام واحد تجاری')),
                ('address', models.TextField(verbose_name='آدرس')),
                ('phone_number', models.CharField(max_length=12, verbose_name='تلفن تماس')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='کاربر فروشنده')),
            ],
            options={
                'verbose_name': 'فروشنده',
                'verbose_name_plural': 'فروشندگان',
            },
        ),
        migrations.CreateModel(
            name='Sells',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='تاریخ ساخت')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='آخرین بروزرسانی')),
                ('is_valid', models.BooleanField(default=True, verbose_name='اولین بار')),
                ('consumer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sell', to='consumers.consumers', verbose_name='مصرف کننده')),
                ('sale_plan', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='sell', to='sales.salesplan', verbose_name='طرح فروش')),
                ('seller', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sell', to='sales.sellers', verbose_name='فروشنده')),
            ],
            options={
                'verbose_name': 'فروش',
                'verbose_name_plural': 'فروش ها',
            },
        ),
        migrations.AddField(
            model_name='salesplan',
            name='sellers',
            field=models.ManyToManyField(to='sales.sellers', verbose_name='فروشندگان طرح'),
        ),
    ]
