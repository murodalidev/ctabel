# Generated by Django 3.2 on 2021-05-05 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0002_alter_construction_description'),
        ('account', '0009_worker'),
    ]

    operations = [
        migrations.AddField(
            model_name='worker',
            name='construction',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='construction.construction', verbose_name='Construction'),
            preserve_default=False,
        ),
    ]
