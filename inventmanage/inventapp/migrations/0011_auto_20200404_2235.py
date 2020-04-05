# Generated by Django 3.0 on 2020-04-04 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventapp', '0010_auto_20200404_2229'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customer',
            old_name='users_id',
            new_name='users',
        ),
        migrations.RenameField(
            model_name='orders',
            old_name='users_id',
            new_name='users',
        ),
        migrations.RenameField(
            model_name='payment',
            old_name='users_id',
            new_name='users',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='users',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='users_id',
            field=models.PositiveIntegerField(default=301),
        ),
    ]
