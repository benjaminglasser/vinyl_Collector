# Generated by Django 3.2.4 on 2021-07-02 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vinyl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
            ],
        ),
    ]
