from tabnanny import verbose
from django.db import models


class Master(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Имя мастера")
    last_name = models.CharField(max_length=40, verbose_name="Фамилия мастера")
    contact_info = models.TextField(max_length=30, verbose_name="Контактная информация")
    photo = models.ImageField(
        blank=True, null=True, upload_to="masters/photos/", verbose_name="Фото мастера"
    )
    services = models.ManyToManyField(
        Service, related_name="name", verbose_name="Услуги"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Мастер"
        verbose_name_plural = "Мастера"


class Service(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название услуги")
    price = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Стоимость"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услуга"
        verbose_name_plural = "Услуги"
