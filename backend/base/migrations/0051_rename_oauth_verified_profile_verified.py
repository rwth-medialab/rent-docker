# Generated by Django 4.1.5 on 2023-01-21 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0050_profile_oauth_verified'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='oauth_verified',
            new_name='verified',
        ),
    ]
