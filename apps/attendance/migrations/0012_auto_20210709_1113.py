# Generated by Django 3.2 on 2021-07-09 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0011_alter_attendance_date_created'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='attendance',
            options={'ordering': ('date_created',), 'verbose_name': 'Attendance', 'verbose_name_plural': ' Attendances'},
        ),
        migrations.AlterModelOptions(
            name='workinghour',
            options={'ordering': ('hour',), 'verbose_name': 'Working Hours', 'verbose_name_plural': '   Working Hours'},
        ),
    ]
