# Generated by Django 4.1.1 on 2022-09-30 10:45

import django.contrib.auth.password_validation
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=20, validators=[django.contrib.auth.password_validation.validate_password]),
        ),
    ]
