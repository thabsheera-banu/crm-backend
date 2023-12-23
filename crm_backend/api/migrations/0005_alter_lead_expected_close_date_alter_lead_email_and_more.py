# Generated by Django 5.0 on 2023-12-19 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_lead_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='Expected_close_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='labels',
            field=models.CharField(blank=True, choices=[('Hot', 'Hot'), ('Warm', 'Warm'), ('Cold', 'Cold')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
