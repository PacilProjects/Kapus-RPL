# Generated by Django 4.1.3 on 2022-12-08 01:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AdministrasiBuku', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perpustakaan',
            fields=[
                ('nama', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('lokasi', models.CharField(max_length=100)),
                ('alamat', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'perpustakaan',
            },
        ),
        migrations.RemoveField(
            model_name='buku',
            name='banyak',
        ),
        migrations.CreateModel(
            name='PerpusBuku',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kuantitas', models.IntegerField(default=0)),
                ('isbn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdministrasiBuku.buku')),
                ('nama_perpus', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AdministrasiBuku.perpustakaan')),
            ],
            options={
                'db_table': 'PerpusBuku',
            },
        ),
        migrations.AddField(
            model_name='buku',
            name='perpustakaan',
            field=models.ManyToManyField(through='AdministrasiBuku.PerpusBuku', to='AdministrasiBuku.perpustakaan'),
        ),
    ]