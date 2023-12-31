# Generated by Django 4.2.5 on 2023-09-25 18:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_alter_company_options'),
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='company',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='companies.company'),
            preserve_default=False,
        ),
    ]
