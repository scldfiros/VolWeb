# Generated by Django 3.2.18 on 2023-04-22 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linux_engine', '0015_sockstat'),
    ]

    operations = [
        migrations.AddField(
            model_name='sockstat',
            name='SourcePort',
            field=models.TextField(null=True),
        ),
    ]
