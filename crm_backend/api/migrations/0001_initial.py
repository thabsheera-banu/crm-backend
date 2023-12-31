# Generated by Django 5.0 on 2023-12-26 05:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pipeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_person', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('labels', models.CharField(blank=True, choices=[('Hot', 'Hot'), ('Warm', 'Warm'), ('Cold', 'Cold')], max_length=20, null=True)),
                ('Expected_close_date', models.DateTimeField(blank=True, null=True)),
                ('value', models.CharField(blank=True, max_length=50, null=True)),
                ('value_mode', models.CharField(blank=True, choices=[('Indian Rupee', 'Indian Rupee'), ('USD', 'USD')], max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_mode', models.CharField(blank=True, choices=[('Work', 'Work'), ('Home', 'Home')], max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('email_mode', models.CharField(blank=True, choices=[('Work', 'Work'), ('Home', 'Home')], max_length=50, null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Deal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_person', models.CharField(max_length=100)),
                ('organization', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField(blank=True, max_length=100, null=True, unique=True)),
                ('labels', models.CharField(blank=True, choices=[('Hot', 'Hot'), ('Warm', 'Warm'), ('Cold', 'Cold')], max_length=20, null=True)),
                ('Expected_close_date', models.DateTimeField(blank=True, null=True)),
                ('value', models.CharField(blank=True, max_length=50, null=True)),
                ('value_mode', models.CharField(blank=True, choices=[('Indian Rupee', 'Indian Rupee'), ('USD', 'USD')], max_length=50, null=True)),
                ('phone', models.CharField(blank=True, max_length=50, null=True)),
                ('phone_mode', models.CharField(blank=True, choices=[('Work', 'Work'), ('Home', 'Home')], max_length=50, null=True)),
                ('email', models.CharField(blank=True, max_length=50, null=True)),
                ('email_mode', models.CharField(blank=True, choices=[('Work', 'Work'), ('Home', 'Home')], max_length=50, null=True)),
                ('pipeline', models.CharField(blank=True, choices=[('Pipeline', 'Pipeline')], max_length=50)),
                ('won', models.BooleanField(default=False)),
                ('lost', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('pipeline_status', models.ManyToManyField(blank=True, to='api.pipeline')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
