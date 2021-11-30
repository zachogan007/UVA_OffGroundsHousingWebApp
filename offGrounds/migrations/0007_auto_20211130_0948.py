# Generated by Django 3.2.7 on 2021-11-30 14:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('offGrounds', '0006_alter_review_pub_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='review',
            name='review_text',
        ),
        migrations.AddField(
            model_name='review',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='review',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviewswrite', to='offGrounds.listing'),
        ),
        migrations.AlterField(
            model_name='review',
            name='pub_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
