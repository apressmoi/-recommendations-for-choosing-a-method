# Generated by Django 3.0.6 on 2020-05-14 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200514_2235'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='typeprint',
            name='paper',
        ),
        migrations.AddField(
            model_name='production',
            name='paper',
            field=models.ManyToManyField(to='core.Paper'),
        ),
    ]
