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
            field=models.DateTimeField(default=datetime.datetime(2021, 11, 23, 1, 45, 44, 743360, tzinfo=utc)),
        ),
    ]