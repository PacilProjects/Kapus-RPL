# Generated by Django 4.1.4 on 2022-12-10 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RatingPerpustakaan', '0006_remove_countrating_nama_perpus_banget'),
    ]

    operations = [
        migrations.AddField(
            model_name='countrating',
            name='nama_perpus_banget',
            field=models.CharField(default=0, max_length=50, verbose_name=()),
            preserve_default=False,
        ),
    ]