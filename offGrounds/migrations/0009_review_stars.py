# Generated by Django 3.2.7 on 2021-11-30 17:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offGrounds', '0008_alter_review_place'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
