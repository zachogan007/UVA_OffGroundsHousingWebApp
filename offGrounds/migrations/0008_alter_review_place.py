# Generated by Django 3.2.7 on 2021-11-30 15:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offGrounds', '0007_auto_20211130_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='offGrounds.listing'),
        ),
    ]
