# Generated by Django 4.0.dev20210216092534 on 2021-03-13 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_posts'),
    ]

    operations = [
        migrations.DeleteModel(
            name='MyModel',
        ),
        migrations.AddField(
            model_name='posts',
            name='Name',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
