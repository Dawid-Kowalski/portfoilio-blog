# Generated by Django 3.0.6 on 2020-05-06 20:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_documments'),
    ]

    operations = [
        migrations.RenameField(
            model_name='documments',
            old_name='descripton_en',
            new_name='description_en',
        ),
    ]