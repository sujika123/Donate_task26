# Generated by Django 4.2.11 on 2024-03-14 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0006_donation'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]