# Generated by Django 2.0.1 on 2018-01-25 15:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthorizationManagement', '0003_auto_20180125_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='owners',
            field=models.ManyToManyField(related_name='owner', to=settings.AUTH_USER_MODEL),
        ),
    ]
