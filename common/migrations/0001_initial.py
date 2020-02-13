# Generated by Django 3.0.2 on 2020-02-13 13:46

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='user.username')),
                ('password', models.CharField(max_length=128, verbose_name='user.password')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='user.first_name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='user.last_name')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='user.email')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='user.last_login')),
                ('is_active', models.BooleanField(default=True, verbose_name='user.is_active')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='user.is_superuser')),
                ('is_staff', models.BooleanField(default=False, verbose_name='user.is_staff')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='user.date_joined')),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
