# Generated by Django 4.1.4 on 2022-12-10 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_logout', '0002_alter_authuserkapus_email_alter_authuserkapus_hp_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuserkapus',
            name='email',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='authuserkapus',
            name='hp',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='authuserkapus',
            name='lokasi',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='authuserkapus',
            name='password',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='authuserkapus',
            name='tipeUser',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='authuserkapus',
            name='username',
            field=models.CharField(max_length=50, primary_key=True, serialize=False, unique=True),
        ),
    ]
