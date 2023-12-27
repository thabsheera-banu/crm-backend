# Generated by Django 5.0 on 2023-12-26 05:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='activity',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='deal',
            name='call',
            field=models.IntegerField(blank=True, default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deal',
            name='notes',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='activity',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='call',
            field=models.IntegerField(blank=True, default='1'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='lead',
            name='notes',
            field=models.TextField(blank=True),
        ),
    ]
