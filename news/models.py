from django.db import models

class Artiles(models.Model):
    title = models.CharField('Название',max_length=40)
    anons = models.CharField('Анонс',max_length=200)
    full_text = models.TextField("Статья")
    date = models.DateTimeField("Дата публикации")

    def __str__(self):
        return f'Новости: {self.title}'

    def get_absolute_url(self):
        return f'/news/{self.id}'

    class Meta:
        verbose_name = 'Жаңалық'
        verbose_name_plural = 'Жаңалықтар'