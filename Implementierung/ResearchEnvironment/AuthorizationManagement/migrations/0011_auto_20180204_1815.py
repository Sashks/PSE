# Generated by Django 2.0.1 on 2018-02-04 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AuthorizationManagement', '0010_auto_20180128_2345'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.AlterField(
            model_name='resource',
            name='link',
            field=models.FileField(upload_to=''),
        ),
    ]