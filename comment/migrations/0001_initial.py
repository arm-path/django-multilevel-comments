# Generated by Django 3.1 on 2020-08-27 08:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_text', models.TextField(max_length=500, verbose_name='Текст коментария')),
                ('like', models.IntegerField(default=0, verbose_name='Мне нравится')),
                ('dislike', models.IntegerField(default=0, verbose_name='Мне не нравится')),
                ('publication_date', models.DateField(auto_now_add=True, verbose_name='Дата публикации')),
                ('update_date', models.DateField(auto_now=True, verbose_name='Дата обновления')),
                ('posted_by', models.BooleanField(default=True, verbose_name='Опубликовано')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('blog', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.blog', verbose_name='Блог')),
                ('dislike_user', models.ManyToManyField(blank=True, related_name='comment_blog_dislake_rn', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи поставившие мне не нравиться')),
                ('like_user', models.ManyToManyField(blank=True, related_name='comment_blog_like_rn', to=settings.AUTH_USER_MODEL, verbose_name='Пользователи поставившие мне нравиться')),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
                ('parent', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='comment.blogcomment', verbose_name='Коментарий')),
            ],
            options={
                'verbose_name': 'Коментария',
                'verbose_name_plural': 'Коментарии',
            },
        ),
    ]
