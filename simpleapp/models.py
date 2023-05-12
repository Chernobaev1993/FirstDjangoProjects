from django.db import models
from django.core.validators import MinValueValidator


class Product(models.Model):
    # названия товаров не должны повторяться
    name = models.CharField(max_length=50, unique=True,)
    description = models.TextField()
    quantity = models.IntegerField(validators=[MinValueValidator(0)],)

    # поле категории будет ссылаться на модель категории
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE, related_name='products',)
    # все продукты в категории будут доступны через поле products

    price = models.FloatField(validators=[MinValueValidator(0.0)],)

    def __str__(self):
        return f'{self.name.title()}: {self.description[:20]}'


# Категория, к которой будет привязываться товар
class Category(models.Model):
    # названия категорий тоже не должны повторяться
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name.title()