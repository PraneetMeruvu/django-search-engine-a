# Generated by Django 4.1.3 on 2024-04-24 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleFileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('files', models.FileField(blank=True, null=True, upload_to='uploads/')),
            ],
        ),
        migrations.DeleteModel(
            name='Excel',
        ),
    ]
