# Generated by Django 2.0.1 on 2018-01-25 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthorizationManagement', '0004_auto_20180125_1659'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resource',
            name='owners',
            field=models.ManyToManyField(related_name='owner', to='AuthorizationManagement.Owner'),
        ),
    ]
