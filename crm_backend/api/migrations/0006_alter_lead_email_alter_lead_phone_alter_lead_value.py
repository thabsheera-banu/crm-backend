# Generated by Django 5.0 on 2023-12-20 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_lead_expected_close_date_alter_lead_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lead',
            name='email',
            field=models.EmailField(blank=True, choices=[('Work', 'Work'), ('Home', 'Home')], max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='phone',
            field=models.IntegerField(blank=True, choices=[('Work', 'Work'), ('Home', 'Home')], null=True),
        ),
        migrations.AlterField(
            model_name='lead',
            name='value',
            field=models.CharField(blank=True, choices=[('Indian Rupee', 'Indian Rupee'), ('USD', 'USD')], max_length=20, null=True),
        ),
    ]