# Generated by Django 3.2 on 2021-05-17 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0002_alter_construction_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='construction',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='Description'),
        ),
    ]
