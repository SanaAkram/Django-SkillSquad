# Generated by Django 3.1.4 on 2022-04-16 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('direct', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
