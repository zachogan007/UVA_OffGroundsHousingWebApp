# Generated by Django 3.2.9 on 2021-11-22 19:46

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('offGrounds', '0006_alter_listing_pub_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 22, 19, 45, 59, 950698, tzinfo=utc)),
        ),
    ]
