# Generated by Django 3.0.7 on 2020-07-20 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0002_destination_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='destination',
            name='place',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
