# Generated by Django 2.0.1 on 2018-01-28 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AuthorizationManagement', '0009_auto_20180128_2344'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='accessrequest',
            unique_together={('sender', 'resource')},
        ),
        migrations.AlterUniqueTogether(
            name='deletionrequest',
            unique_together={('sender', 'resource')},
        ),
    ]
