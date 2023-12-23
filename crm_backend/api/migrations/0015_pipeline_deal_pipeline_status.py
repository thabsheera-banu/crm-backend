# Generated by Django 5.0 on 2023-12-21 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_remove_deal_pipeline_status_deal_expected_close_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pipeline',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='deal',
            name='pipeline_status',
            field=models.ManyToManyField(blank=True, to='api.pipeline'),
        ),
    ]
