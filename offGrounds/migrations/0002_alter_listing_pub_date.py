# Generated by Django 3.2.9 on 2021-11-12 18:29

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('offGrounds', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 12, 18, 29, 11, 758509, tzinfo=utc)),
        ),
    ]