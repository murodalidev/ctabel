# Generated by Django 3.2 on 2021-05-06 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20210506_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.position', verbose_name='worker position'),
        ),
    ]
