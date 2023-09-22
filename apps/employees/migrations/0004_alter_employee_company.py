# Generated by Django 4.2.5 on 2023-09-22 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_alter_company_options'),
        ('employees', '0003_alter_employee_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='company',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='companies.company'),
        ),
    ]