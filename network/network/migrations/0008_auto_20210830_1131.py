# Generated by Django 3.2 on 2021-08-30 11:31

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_auto_20210830_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='last_editted',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='post',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
