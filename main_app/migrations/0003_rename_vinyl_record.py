# Generated by Django 3.2.5 on 2021-07-16 01:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20210715_2230'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Vinyl',
            new_name='Record',
        ),
    ]
