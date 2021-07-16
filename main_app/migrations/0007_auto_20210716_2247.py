# Generated by Django 3.2.5 on 2021-07-16 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_artist_record'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artist',
            name='record',
        ),
        migrations.AddField(
            model_name='record',
            name='artists',
            field=models.ManyToManyField(to='main_app.Artist'),
        ),
    ]