# Generated by Django 4.1.4 on 2022-12-10 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RatingPerpustakaan', '0007_countrating_nama_perpus_banget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrating',
            name='nama_perpus_banget',
            field=models.CharField(max_length=50, verbose_name=()),
        ),
    ]