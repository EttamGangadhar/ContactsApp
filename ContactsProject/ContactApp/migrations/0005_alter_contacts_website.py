# Generated by Django 4.2 on 2023-06-13 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactApp', '0004_contacts_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='website',
            field=models.CharField(max_length=100),
        ),
    ]
