# Generated by Django 4.1.4 on 2022-12-10 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_logout', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuserkapus',
            name='email',
            field=models.CharField(default='email', max_length=50),
        ),
        migrations.AlterField(
            model_name='authuserkapus',
            name='hp',
            field=models.CharField(default='123', max_length=50),
        ),
        migrations.AlterField(
            model_name='authuserkapus',
            name='lokasi',
            field=models.CharField(default='lokasi', max_length=50),
        ),
        migrations.AlterField(
            model_name='authuserkapus',
            name='password',
            field=models.CharField(default='password', max_length=50),
        ),
        migrations.AlterField(
            model_name='authuserkapus',
            name='tipeUser',
            field=models.CharField(default='tipeUser', max_length=50),
        ),
        migrations.AlterField(
            model_name='authuserkapus',
            name='username',
            field=models.CharField(default='username', max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
