# Generated by Django 4.2 on 2023-06-13 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ContactApp', '0003_alter_contacts_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='image',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
