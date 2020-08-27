from django.db import models
from django.urls import reverse


class Blog(models.Model):
    """ Модель Блога """
    title = models.CharField('Название', max_length=150, unique=True)
    slug = models.SlugField('URL', max_length=150, unique=True)
    created_at = models.DateField('Дата', auto_now_add=True)
    posted_by = models.BooleanField('Опубликовано', default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_page', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['-created_at', ]
