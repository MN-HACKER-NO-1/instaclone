# Generated by Django 3.0.6 on 2020-05-10 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0002_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='last_login',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
