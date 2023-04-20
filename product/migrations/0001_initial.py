# Generated by Django 4.1.3 on 2023-04-13 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=200)),
                ('language', models.CharField(max_length=200)),
                ('genre', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('min_age', models.IntegerField()),
                ('price', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
