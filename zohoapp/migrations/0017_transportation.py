# Generated by Django 4.2 on 2023-08-17 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0016_alter_payroll_emp_number'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transportation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=100)),
            ],
        ),
    ]
