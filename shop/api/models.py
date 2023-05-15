from django.db import models

# Create your models here.


class Book(models.Model):
    Book_name = models.CharField(max_length=255, unique=True, verbose_name="Кітап атауы")
    author = models.CharField(max_length=255, verbose_name="Автор")
    photo = models.ImageField(upload_to='img', verbose_name="Фото")
    desc = models.CharField(max_length=1024, verbose_name="Сипаттамасы")
    genre = models.CharField(max_length=255, verbose_name="Жанр")
    price = models.IntegerField(verbose_name="Бағасы")
    pieces = models.IntegerField(verbose_name="Дана")

    def __str__(self):
        return self.Book_name

