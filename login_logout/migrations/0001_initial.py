# Generated by Django 4.1.3 on 2022-12-02 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuthUserKapus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('lokasi', models.CharField(max_length=50)),
                ('hp', models.CharField(max_length=50)),
                ('tipeUser', models.CharField(max_length=50)),
            ],
        ),
    ]