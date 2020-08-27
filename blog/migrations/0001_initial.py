# Generated by Django 3.1 on 2020-08-27 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, unique=True, verbose_name='Название')),
                ('slug', models.SlugField(max_length=150, unique=True, verbose_name='URL')),
                ('created_at', models.DateField(auto_now_add=True, verbose_name='Дата')),
                ('posted_by', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Блог',
                'verbose_name_plural': 'Блоги',
                'ordering': ['-created_at'],
            },
        ),
    ]
