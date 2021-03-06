# Generated by Django 3.1.7 on 2021-02-27 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lectures', '0002_auto_20210227_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='lecture',
            name='duration',
            field=models.IntegerField(default=2, help_text='Enter number of hours'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lecture',
            name='is_required',
            field=models.BooleanField(default=True),
        ),
    ]
