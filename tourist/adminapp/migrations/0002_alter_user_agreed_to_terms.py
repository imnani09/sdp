# Generated by Django 5.0.3 on 2024-03-08 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='agreed_to_terms',
            field=models.CharField(max_length=10),
        ),
    ]
