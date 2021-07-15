# Generated by Django 3.2 on 2021-06-08 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0007_alter_construction_object'),
        ('attendance', '0006_attendance_construction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='construction',
            field=models.ForeignKey(blank=True, limit_choices_to={'status': 0}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='attendances', to='construction.construction', verbose_name='Construction'),
        ),
    ]
