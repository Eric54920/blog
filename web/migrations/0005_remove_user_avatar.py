# Generated by Django 2.2.5 on 2020-04-20 16:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_auto_20200421_0025'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='avatar',
        ),
    ]
