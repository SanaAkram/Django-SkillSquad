# Generated by Django 3.1.4 on 2022-04-19 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authy', '0002_auto_20220416_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='email',
            field=models.EmailField(default='mymail@gmail.com', max_length=254),
        ),
    ]
