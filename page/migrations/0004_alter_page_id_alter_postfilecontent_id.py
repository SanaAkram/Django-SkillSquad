# Generated by Django 4.0.4 on 2022-04-27 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0003_page_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='postfilecontent',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]