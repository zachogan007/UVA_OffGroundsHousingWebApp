import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('num_beds', models.IntegerField(default=0)),
                ('num_baths', models.FloatField(default=0.0)),
                ('rent', models.FloatField(default=0.0)),
                ('size', models.FloatField(default=0.0)),
                ('longitude', models.FloatField(default=0.0)),
                ('latitude', models.FloatField(default=0.0)),
                ('pub_date', models.DateTimeField(default=datetime.datetime(2021, 11, 22, 23, 13, 49, 814371, tzinfo=utc))),
                ('image', models.ImageField(upload_to='images')),
                ('laundry', models.CharField(blank=True, default='', max_length=200)),
                ('parking', models.CharField(blank=True, default='', max_length=200)),
                ('fitness', models.CharField(blank=True, default='', max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField(max_length=20000)),
                ('pub_date', models.DateField(verbose_name='date published')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=2000)),
                ('password', models.TextField(default='', max_length=2000)),
            ],
        ),
    ]