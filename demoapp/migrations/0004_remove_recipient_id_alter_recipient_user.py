# Generated by Django 4.2.11 on 2024-03-14 04:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0003_alter_recipient_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipient',
            name='id',
        ),
        migrations.AlterField(
            model_name='recipient',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='Recipient', serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]