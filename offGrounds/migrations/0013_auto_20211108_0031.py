# Generated by Django 3.2.7 on 2021-11-08 05:31

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('offGrounds', '0012_alter_listing_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='listing',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 8, 5, 31, 46, 794538, tzinfo=utc)),
        ),
    ]
