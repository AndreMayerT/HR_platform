# Generated by Django 4.2.5 on 2023-09-25 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_alter_document_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file',
            field=models.FileField(default='', upload_to='documents'),
            preserve_default=False,
        ),
    ]
