# Generated by Django 4.1.5 on 2023-02-13 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_listings_image_url_alter_listings_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listings',
            name='title',
            field=models.CharField(max_length=64),
        ),
    ]