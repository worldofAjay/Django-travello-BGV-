# Generated by Django 3.0.7 on 2020-07-26 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BGV', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resources',
            name='CID',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resources',
            name='ContactNumber',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='resources',
            name='TMTRequest',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]