# Generated by Django 3.2 on 2021-05-05 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('construction', '0002_alter_construction_description'),
        ('account', '0006_auto_20210505_1314'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'verbose_name': 'Account', 'verbose_name_plural': '   Accounts'},
        ),
        migrations.AlterModelOptions(
            name='headerworker',
            options={'verbose_name': 'Header worker', 'verbose_name_plural': '  Header workers'},
        ),
        migrations.AlterModelOptions(
            name='position',
            options={'verbose_name': 'Position', 'verbose_name_plural': 'Positions'},
        ),
        migrations.AlterModelOptions(
            name='subworker',
            options={'verbose_name': 'Sub worker', 'verbose_name_plural': ' Sub workers'},
        ),
        migrations.AlterField(
            model_name='headerworker',
            name='construction',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='construction.construction', verbose_name='Construction'),
            preserve_default=False,
        ),
    ]
