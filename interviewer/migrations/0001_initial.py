# Generated by Django 3.1.4 on 2022-04-19 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authy', '0003_profile_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Interviewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authy.profile')),
            ],
        ),
    ]
