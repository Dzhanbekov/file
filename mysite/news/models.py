from django.db import models

class News(models.Model):
    title = models.CharField(max_length=150, verbose_name='наименование')
    content = models.TextField(blank=True, verbose_name='контент')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата публикации')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='обновлено')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', verbose_name='фото', blank=True)
    is_published = models.BooleanField(default=True, verbose_name='опубликовано')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name='Категория')



    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
        ordering = ["-created_at"]


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='наименование категории')

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категорти"
        ordering = ["title"]