# Generated by Django 3.2 on 2021-05-05 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Username')),
                ('email', models.EmailField(db_index=True, max_length=50, unique=True, verbose_name='Email')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='Super user')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Stuff user')),
                ('is_active', models.BooleanField(default=True, verbose_name='Active user')),
                ('date_login', models.DateTimeField(auto_now=True, verbose_name='Last login')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Created date')),
            ],
            options={
                'verbose_name': 'Account',
                'verbose_name_plural': 'Accounts',
            },
        ),
    ]
