# Generated by Django 3.1.4 on 2020-12-21 08:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='date_updated',
        ),
    ]
