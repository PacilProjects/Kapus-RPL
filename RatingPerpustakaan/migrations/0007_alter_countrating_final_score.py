# Generated by Django 4.1.3 on 2022-12-10 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RatingPerpustakaan', '0006_alter_countrating_nama_perpus_banget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='countrating',
            name='final_score',
            field=models.FloatField(),
        ),
    ]
