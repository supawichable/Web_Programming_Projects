# Generated by Django 3.2 on 2021-08-18 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0013_auto_20210818_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bid',
            name='bid_item',
        ),
        migrations.AddField(
            model_name='bid',
            name='bid_item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='bidding', to='auctions.listing'),
        ),
        migrations.RemoveField(
            model_name='comment',
            name='comment_item',
        ),
        migrations.AddField(
            model_name='comment',
            name='comment_item',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='commenting', to='auctions.listing'),
        ),
    ]
