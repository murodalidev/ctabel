# Generated by Django 3.2 on 2021-07-13 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0004_door_direction'),
    ]

    operations = [
        migrations.AlterField(
            model_name='door',
            name='direction',
            field=models.IntegerField(choices=[(0, 'Login'), (1, 'Logout')], verbose_name='Door direction'),
        ),
    ]
