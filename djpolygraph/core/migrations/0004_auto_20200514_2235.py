# Generated by Django 3.0.6 on 2020-05-14 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200514_2226'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='circulation',
            name='count',
        ),
        migrations.AddField(
            model_name='circulation',
            name='max_count',
            field=models.IntegerField(default=1, verbose_name='Максимальное кол-во'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='circulation',
            name='min_count',
            field=models.IntegerField(default=1, verbose_name='Минимальное кол-во'),
            preserve_default=False,
        ),
    ]
