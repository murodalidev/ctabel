# Generated by Django 3.2 on 2021-07-13 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('terminal', '0007_person_terminal'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='person',
            name='terminal',
        ),
        migrations.AddField(
            model_name='person',
            name='terminal',
            field=models.ManyToManyField(blank=True, null=True, to='terminal.Terminal', verbose_name='Terminal'),
        ),
    ]
