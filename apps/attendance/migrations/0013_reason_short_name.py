# Generated by Django 3.2 on 2021-07-15 06:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0012_auto_20210709_1113'),
    ]

    operations = [
        migrations.AddField(
            model_name='reason',
            name='short_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=4, verbose_name='Short name of reason'),
            preserve_default=False,
        ),
    ]
