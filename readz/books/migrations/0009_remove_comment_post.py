# Generated by Django 4.0.dev20210216092534 on 2021-03-26 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_alter_comment_body'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='post',
        ),
    ]
