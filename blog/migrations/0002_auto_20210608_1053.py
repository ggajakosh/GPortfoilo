# Generated by Django 2.2.19 on 2021-06-08 05:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='description',
            new_name='description1',
        ),
    ]