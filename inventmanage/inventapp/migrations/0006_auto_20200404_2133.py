# Generated by Django 3.0 on 2020-04-04 16:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventapp', '0005_auto_20200404_2128'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='users_id',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='customer',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_customer', to='inventapp.UserProfile'),
        ),
    ]
