from django.db import models
from django.contrib.auth.models import User
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from blog.models import Blog


class BlogComment(MPTTModel):
    """  Модель комментарий """
    name = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.CASCADE, verbose_name='Пользователь')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True,
                            blank=True, related_name='children', verbose_name='Коментарий')
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, verbose_name='Блог', null=True, blank=True)
    comment_text = models.TextField('Текст коментария', max_length=500)
    like = models.IntegerField('Мне нравится', default=0)
    like_user = models.ManyToManyField(User, related_name='comment_blog_like_rn',
                                       verbose_name="Пользователи поставившие мне нравиться", blank=True)
    dislike = models.IntegerField('Мне не нравится', default=0)
    dislike_user = models.ManyToManyField(
        User, related_name='comment_blog_dislake_rn', verbose_name="Пользователи поставившие мне не нравиться", blank=True)
    publication_date = models.DateField('Дата публикации', auto_now_add=True)
    update_date = models.DateField('Дата обновления', auto_now=True)
    posted_by = models.BooleanField('Опубликовано', default=True)

    def __str__(self):
        return str(self.name) + ': ' + self.comment_text[:25] + '...'

    class MPTTMeta:
        order_insertion_by = ['-publication_date']

    class Meta:
        verbose_name = 'Коментария'
        verbose_name_plural = 'Коментарии'
