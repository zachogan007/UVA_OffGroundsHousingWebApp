# Generated by Django 3.2.7 on 2021-11-30 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('offGrounds', '0009_review_stars'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='pub_date',
        ),
    ]
