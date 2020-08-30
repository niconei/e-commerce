# Generated by Django 3.1 on 2020-08-30 21:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0016_auto_20200830_2140'),
    ]

    operations = [
        migrations.AddField(
            model_name='bids',
            name='listing',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='bid_listing', to='auctions.listing'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bids',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='bid_user', to='auctions.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='content',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='comments',
            name='listing',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='comment_listing', to='auctions.listing'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='category',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='current_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
        ),
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='detail_one',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='listing',
            name='detail_three',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='listing',
            name='detail_two',
            field=models.CharField(blank=True, max_length=64),
        ),
        migrations.AddField(
            model_name='listing',
            name='image_url',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='starting_bid',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='title',
            field=models.CharField(default=1, max_length=64),
            preserve_default=False,
        ),
    ]