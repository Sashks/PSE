# Generated by Django 2.0.1 on 2018-01-26 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AuthorizationManagement', '0002_auto_20180122_2016'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resource',
            old_name='owner',
            new_name='owners',
        ),
        migrations.AlterField(
            model_name='accessrequest',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AuthorizationManagement.Resource'),
        ),
        migrations.AlterField(
            model_name='accessrequest',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AuthorizationManagement.CustomUser'),
        ),
        migrations.AlterField(
            model_name='deletionrequest',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AuthorizationManagement.Resource'),
        ),
        migrations.AlterField(
            model_name='deletionrequest',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='AuthorizationManagement.CustomUser'),
        ),
    ]
