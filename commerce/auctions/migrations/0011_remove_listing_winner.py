# Generated by Django 3.2 on 2021-08-18 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_remove_listing_max_bidder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='listing',
            name='winner',
        ),
    ]
