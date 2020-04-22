# Generated by Django 2.2.5 on 2020-04-21 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0009_auto_20200421_0058'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='realmaguodong@outlook.com', max_length=254, verbose_name='邮箱'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='user',
            name='web_site',
            field=models.URLField(default='https://maguodong.com', verbose_name='网址'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.URLField(verbose_name='头像'),
        ),
    ]
