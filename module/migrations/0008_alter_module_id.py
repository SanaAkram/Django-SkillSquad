# Generated by Django 4.0.4 on 2022-04-27 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0007_remove_module_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]