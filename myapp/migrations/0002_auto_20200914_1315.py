# Generated by Django 3.0.7 on 2020-09-14 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='content_text',
            field=models.FileField(null=True, upload_to='myapp/files'),
        ),
    ]
