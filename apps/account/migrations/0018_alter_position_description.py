# Generated by Django 3.2 on 2021-05-17 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20210517_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='position',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description position'),
        ),
    ]
