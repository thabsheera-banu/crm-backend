# Generated by Django 5.0 on 2023-12-21 08:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_pipeline_remove_deal_expected_close_date_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='pipeline_status',
        ),
        migrations.AddField(
            model_name='deal',
            name='Expected_close_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='deal',
            name='contact_person',
            field=models.CharField(default='timezone.now', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deal',
            name='email',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='deal',
            name='email_mode',
            field=models.CharField(blank=True, choices=[('Work', 'Work'), ('Home', 'Home')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='deal',
            name='labels',
            field=models.CharField(blank=True, choices=[('Hot', 'Hot'), ('Warm', 'Warm'), ('Cold', 'Cold')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='deal',
            name='organization',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deal',
            name='owner',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deal',
            name='phone',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='deal',
            name='phone_mode',
            field=models.CharField(blank=True, choices=[('Work', 'Work'), ('Home', 'Home')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='deal',
            name='slug',
            field=models.SlugField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='deal',
            name='title',
            field=models.CharField(default='1', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='deal',
            name='value',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='deal',
            name='value_mode',
            field=models.CharField(blank=True, choices=[('Indian Rupee', 'Indian Rupee'), ('USD', 'USD')], max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='Pipeline',
        ),
    ]
