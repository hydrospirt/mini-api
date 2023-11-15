from django.db import models


class TextFile(models.Model):
    name = models.CharField(
        max_length=56,
        verbose_name='Имя файла',
        help_text='Добавьте название вашего файла'
    )
    data = models.TextField(
        verbose_name='Содержимое файла'
    )
    pub_date = models.DateTimeField(
        verbose_name='Дата создания',
        auto_now_add=True
    )

    class Meta:
        verbose_name = 'Текстовый файл'
        verbose_name_plural = 'Текстовые файлы'

    def __str__(self) -> str:
        return self.name
