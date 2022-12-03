# Generated by Django 4.1.3 on 2022-12-03 07:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookBorrow',
            fields=[
                ('id_borrow', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='name', max_length=50)),
                ('timestamp_accepted', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('status', models.CharField(default='Siap Diambil', max_length=50)),
                ('timestamp_return_limit', models.DateField(blank=True, default=datetime.date(2022, 12, 10))),
                ('timestamp_retrieval_limit', models.DateField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RequestBooking',
            fields=[
                ('id_booking', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(default='name', max_length=50)),
                ('timestamp_request', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('is_reviewed', models.BooleanField(default=False)),
                ('is_accepted', models.BooleanField(default=False)),
                ('book', models.CharField(default='buku', max_length=50)),
            ],
        ),
    ]
