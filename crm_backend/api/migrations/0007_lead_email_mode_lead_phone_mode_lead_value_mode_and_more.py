# Generated by Django 5.0 on 2023-12-20 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_alter_lead_email_alter_lead_phone_alter_lead_value'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='email_mode',
            field=models.CharField(blank=True, choices=[('Work', 'Work'), ('Home', 'Home')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='phone_mode',
            field=models.CharField(blank=True, choices=[('Work', 'Work'), ('Home', 'Home')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='lead',
            name='value_mode',
            field=models.CharField(blank=True, choices=[('Indian Rupee', 'Indian Rupee'), ('USD', 'USD')], max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='email',
            field=models.EmailField(blank=True, max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='phone',
            field=models.IntegerField(blank=True, max_length=12, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='value',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]