# Generated by Django 2.0.7 on 2018-08-30 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='reg',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='Registration'),
        ),
    ]