# Generated by Django 3.2 on 2021-05-24 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_alter_worker_construction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker',
            name='position',
            field=models.ForeignKey(blank=True, limit_choices_to={'status': 0}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='position_workers', to='account.position', verbose_name='worker position'),
        ),
    ]
