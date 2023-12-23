# Generated by Django 5.0 on 2023-12-20 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_labels_remove_lead_labels_lead_labels'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lead',
            name='labels',
        ),
        migrations.DeleteModel(
            name='Labels',
        ),
        migrations.AddField(
            model_name='lead',
            name='labels',
            field=models.CharField(blank=True, choices=[('Hot', 'Hot'), ('Warm', 'Warm'), ('Cold', 'Cold')], max_length=20, null=True),
        ),
    ]