# Generated by Django 3.2.19 on 2023-07-28 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0010_payroll_attachment'),
    ]

    operations = [
        migrations.AddField(
            model_name='payroll',
            name='TDS',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='payroll',
            name='isTDS',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
