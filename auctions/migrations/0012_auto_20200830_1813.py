# Generated by Django 3.1 on 2020-08-30 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0011_auto_20200830_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='owner_id',
            new_name='user_id',
        ),
        migrations.AddField(
            model_name='comments',
            name='user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='comment_user', to='auctions.user'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='watchlist',
            name='user_id',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='watchlist_user', to='auctions.user'),
            preserve_default=False,
        ),
    ]
