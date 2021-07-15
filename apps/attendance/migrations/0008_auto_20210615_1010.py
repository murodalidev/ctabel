# Generated by Django 3.2 on 2021-06-15 05:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0007_alter_attendance_construction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'verbose_name': 'Attendance', 'verbose_name_plural': ' Attendances'},
        ),
        migrations.AddField(
            model_name='attendance',
            name='context',
            field=models.TextField(blank=True, null=True, verbose_name='Context'),
        ),
        migrations.AddField(
            model_name='attendance',
            name='reason',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='attendance.reason', verbose_name='Reason'),
        ),
        migrations.DeleteModel(
            name='ReasonToNoAttendance',
        ),
    ]