# Generated by Django 4.1.3 on 2022-12-01 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id_booking', models.AutoField(primary_key=True, serialize=False)),
                ('status_booking', models.CharField(max_length=30)),
            ],
        ),
    ]