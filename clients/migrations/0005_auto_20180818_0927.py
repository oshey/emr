# Generated by Django 2.0.7 on 2018-08-18 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0004_auto_20180817_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='prim_tel',
            field=models.CharField(blank=True, max_length=20, verbose_name='primary Tel'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='sec_tel',
            field=models.CharField(blank=True, max_length=20, verbose_name='secondary Tel'),
        ),
    ]
