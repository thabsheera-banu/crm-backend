# Generated by Django 5.0 on 2023-12-21 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_deal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pipeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='deal',
            name='Expected_close_date',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='contact_person',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='email',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='email_mode',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='labels',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='organization',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='phone_mode',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='slug',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='title',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='value',
        ),
        migrations.RemoveField(
            model_name='deal',
            name='value_mode',
        ),
        migrations.AddField(
            model_name='deal',
            name='pipeline_status',
            field=models.ManyToManyField(blank=True, to='api.pipeline'),
        ),
    ]
