from django.contrib.auth.models import User, AbstractUser
from django.db import models
from datetime import timedelta

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


class Order(models.Model):
    book = models.CharField(max_length=1024)
    created_at = models.DateField(auto_now_add=True)
    due_date = models.DateField()
    address = models.CharField(max_length=30, verbose_name="Мекен жайы")
    city = models.CharField(max_length=20, verbose_name="Қала")
    buyers = models.ForeignKey(User, on_delete=models.CASCADE)
    arrived = models.BooleanField(default=False)
    returned = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if not self.due_date:
            self.due_date = self.created_at + timedelta(days=7)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Order {self.id} - Buyer: {self.buyers.username}"


class Deposite(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    deposite = models.IntegerField(default=0)
