# Generated by Django 3.1.7 on 2021-03-14 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0005_auto_20210314_1422'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='use_collection',
            new_name='user_collection',
        ),
    ]
