# Generated by Django 2.0.1 on 2018-01-28 22:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AuthorizationManagement', '0008_auto_20180128_2335'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='accessrequest',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='deletionrequest',
            unique_together=set(),
        ),
    ]
