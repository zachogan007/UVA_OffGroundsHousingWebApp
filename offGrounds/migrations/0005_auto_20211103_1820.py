# Generated by Django 3.2.7 on 2021-11-03 22:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offGrounds', '0004_housing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='housing',
            name='address',
            field=models.TextField(default='', max_length=2000),
        ),
        migrations.AlterField(
            model_name='housing',
            name='description',
            field=models.TextField(default='', max_length=2000),
        ),
    ]