# Generated by Django 2.2.3 on 2021-09-06 01:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20210903_0740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='locality',
            new_name='address',
        ),
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
