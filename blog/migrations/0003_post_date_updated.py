# Generated by Django 3.1.4 on 2020-12-21 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_post_date_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_updated',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]