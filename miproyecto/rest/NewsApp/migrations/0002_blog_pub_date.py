# Generated by Django 3.1.3 on 2020-11-11 12:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('NewsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='pub_date',
            field=models.DateField(default=datetime.datetime(2020, 11, 11, 12, 17, 3, 373673, tzinfo=utc)),
        ),
    ]
