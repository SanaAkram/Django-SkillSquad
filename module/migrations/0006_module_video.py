# Generated by Django 3.1.4 on 2022-04-19 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0005_auto_20220416_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='module',
            name='video',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
