# Generated by Django 4.1.3 on 2024-04-26 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_multiplefileupload_delete_excel'),
    ]

    operations = [
        migrations.AddField(
            model_name='multiplefileupload',
            name='content',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AddField(
            model_name='multiplefileupload',
            name='position_index',
            field=models.JSONField(blank=True, default=dict, null=True),
        ),
        migrations.AddField(
            model_name='multiplefileupload',
            name='title',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
