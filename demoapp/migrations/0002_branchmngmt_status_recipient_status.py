# Generated by Django 4.2.11 on 2024-03-13 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='branchmngmt',
            name='status',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='recipient',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]
