from django.contrib.auth import get_user_model
from django.db import models

from core.models import BaseModel
from .constants import MAX_LENGTH_TITLE, MAX_LENGTH_SLUG

User = get_user_model()


class Category(BaseModel):
    title = models.CharField(
        'Заголовок',
        max_length=MAX_LENGTH_TITLE,
        help_text='Тематическая категория, не более 256 символов'
    )
    description = models.TextField(
        'Описание',
        help_text='Введите описание категории'
    )
    slug = models.SlugField(
        'Идентификатор',
        max_length=MAX_LENGTH_SLUG,
        unique=True,
        help_text='Идентификатор страницы для URL; разрешены символы '
        'латиницы, цифры, дефис и подчёркивание.'
    )

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

    def __str__(self):
        return self.title


class Location(BaseModel):
    name = models.CharField(
        'Название места',
        max_length=MAX_LENGTH_TITLE,
        help_text='Географическая метка, не более 256 символов'
    )

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'
        ordering = ['name']

    def __str__(self):
        return self.name


class Post(BaseModel):
    title = models.CharField(
        'Заголовок',
        max_length=MAX_LENGTH_TITLE,
        help_text='Заголовок поста, не более 256 символов'
    )
    text = models.TextField(
        'Текст',
        help_text='Введите текст, который хотите опубликовать'
    )
    pub_date = models.DateTimeField(
        'Дата и время публикации',
        help_text='Если установить дату и время в будущем — '
        'можно делать отложенные публикации.'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        help_text='Автор публикации',
        verbose_name='Автор публикации'
    )
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        help_text='Географическая метка',
        verbose_name='Местоположение'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        blank=False,
        related_name='posts',
        help_text='Тематическая категория',
        verbose_name='Категория'
    )

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
