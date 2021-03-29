# Generated by Django 4.0.dev20210216092534 on 2021-03-27 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_remove_comment_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='horror',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book1_id', models.IntegerField()),
                ('Name', models.TextField(max_length=50)),
                ('descritption', models.TextField(max_length=500)),
                ('image1', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='mystery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book1_id', models.IntegerField()),
                ('Name', models.TextField(max_length=50)),
                ('descritption', models.TextField(max_length=500)),
                ('image1', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='romantic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book1_id', models.IntegerField()),
                ('Name', models.TextField(max_length=50)),
                ('descritption', models.TextField(max_length=500)),
                ('image1', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='travel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book1_id', models.IntegerField()),
                ('Name', models.TextField(max_length=50)),
                ('descritption', models.TextField(max_length=500)),
                ('image1', models.ImageField(upload_to='')),
            ],
        ),
    ]
