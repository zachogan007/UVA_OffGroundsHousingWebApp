# Generated by Django 3.2.7 on 2021-11-07 20:19

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offGrounds', '0009_auto_20211105_1604'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='pub_date',
            field=models.DateTimeField(default=datetime.date(2021, 11, 7)),
        ),
    ]