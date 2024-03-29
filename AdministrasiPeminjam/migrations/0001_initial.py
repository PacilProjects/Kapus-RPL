# Generated by Django 4.1.3 on 2022-12-04 09:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('AdministrasiBuku', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PeminjamanOffline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True, null=True)),
                ('nama_buku', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AdministrasiBuku.buku')),
                ('perpustakaan', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='AdministrasiBuku.perpustakaan')),
            ],
            options={
                'db_table': 'PeminjamanOffline',
            },
        ),
    ]
