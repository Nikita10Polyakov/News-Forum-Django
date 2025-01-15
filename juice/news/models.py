from django.db import models

class Articles(models.Model):
    title = models.CharField('Развание', max_length=50, default='Без названия')
    anons = models.CharField('Анонс', max_length=250, default='Без названия')
    full_text = models.TextField('Стаья')
    data = models.DateTimeField('Дата публикации')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'