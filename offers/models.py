from django.contrib.auth import get_user_model
from django.db.models import (
    Model,
    CharField,
    IntegerField,
    ForeignKey,
    CASCADE,
    ManyToManyField,
    DateTimeField,
    UniqueConstraint,
)
from django.forms import SlugField

from offers.constants import MAX_LENGTH_CHAR_FIELD, MAX_DISPLAY_SYMBOLS, MAX_LENGTH_SLUG_FIELD

Profile = get_user_model()


class Catalog(Model):
    pass


class Region(Model):
    name = CharField(max_length=MAX_LENGTH_CHAR_FIELD, verbose_name='Название региона')
    code = IntegerField(verbose_name='Код региона', default=0)

    class Meta:
        verbose_name_plural = 'Регионы'
        verbose_name = 'Регион'
        ordering = ['name']

    def __str__(self):
        return self.name


class City(Model):
    name = CharField(max_length=MAX_LENGTH_CHAR_FIELD, verbose_name='Название города')
    population = IntegerField(verbose_name='Население', default=0)
    region = ForeignKey(Region, on_delete=CASCADE, verbose_name='Регион', related_name='cities')

    class Meta:
        verbose_name_plural = 'Города'
        verbose_name = 'Город'
        ordering = ['name']

    def __str__(self):
        return self.name


class Tag(Model):
    name = CharField(max_length=MAX_LENGTH_CHAR_FIELD, verbose_name='Название тега')
    slug = SlugField(max_length=MAX_LENGTH_SLUG_FIELD)

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'
        ordering = ['name']

    def __str__(self):
        return self.name


class Offer(Model):
    name = CharField(max_length=MAX_LENGTH_CHAR_FIELD, verbose_name='Название предложения')
    description = CharField(max_length=1000, verbose_name='Описание')
    city = ForeignKey(City, on_delete=CASCADE, verbose_name='Город', related_name='offers')
    tags = ManyToManyField(Tag, verbose_name='Теги')
    created_at = DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = DateTimeField(auto_now=True, verbose_name='Дата обновления')
    expired_at = DateTimeField(verbose_name='Дата окончания')
    author = ForeignKey(Profile, on_delete=CASCADE, verbose_name='Автор', related_name='offers')

    class Meta:
        verbose_name_plural = 'Предложения'
        verbose_name = 'Предложение'
        ordering = ['name']

    def __str__(self):
        return self.name[:MAX_DISPLAY_SYMBOLS]


class Comment(Model):
    text = CharField(max_length=1000, verbose_name='Текст комментария')
    offer = ForeignKey(Offer, on_delete=CASCADE, verbose_name='Предложение', related_name='comments')
    author = ForeignKey(Profile, on_delete=CASCADE, verbose_name='Автор')
    created_at = DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name_plural = 'Комментарии'
        verbose_name = 'Комментарий'
        ordering = ['created_at']

    def __str__(self):
        return self.text[:MAX_DISPLAY_SYMBOLS]


class Like(Model):
    author = ForeignKey(Profile, on_delete=CASCADE, verbose_name='Автор', related_name='likes')
    offer = ForeignKey(Offer, on_delete=CASCADE, verbose_name='Предложение', related_name='likes')
    created_at = DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        verbose_name_plural = 'Лайки'
        verbose_name = 'Лайк'
        ordering = ['author']
        constraints = [
            UniqueConstraint(fields=['author', 'offer'], name='unique_like')
        ]

    def __str__(self):
        return f'{self.author} - {self.offer}'
from django.db.models import Model


class Review(Model):
    pass

