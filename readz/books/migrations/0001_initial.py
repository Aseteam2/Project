# Generated by Django 4.0.dev20210216092534 on 2021-03-18 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='posts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Comment', models.TextField(blank=True)),
                ('Name', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='user_collection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(blank=True)),
                ('image', models.ImageField(upload_to='images')),
            ],
        ),
    ]
