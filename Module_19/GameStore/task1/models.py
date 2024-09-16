from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=100, unique=True)  # Имя покупателя
    balance = models.DecimalField(max_digits=10, decimal_places=2)  # Баланс
    age = models.PositiveIntegerField()  # Возраст

    def __str__(self):
        return self.name


class Game(models.Model):
    title = models.CharField(max_length=200)  # Название игры
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Цена
    size = models.DecimalField(max_digits=10, decimal_places=2)  # Размер файлов
    description = models.TextField()  # Описание игры
    age_limited = models.BooleanField(default=False)  # 18+ ограничение
    buyers = models.ManyToManyField(Buyer, related_name='games')  # Покупатели, обладающие игрой

    def __str__(self):
        return self.title
