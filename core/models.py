from tabnanny import verbose
from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=255, verbose_name="Наименование")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Услугу"
        verbose_name_plural = "Услуги"


class Master(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Имя мастера")
    last_name = models.CharField(max_length=40, verbose_name="Фамилия мастера")
    contact_info = models.TextField(max_length=30, verbose_name="Контактная информация")
    photo = models.ImageField(
        blank=True,
        null=True,
        upload_to="masters/photos/",
        verbose_name="Фото мастера",
    )
    services = models.ManyToManyField(Service, related_name="masters")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = "Мастера"
        verbose_name_plural = "Мастера"


class Client(models.Model):
    name = models.CharField(max_length=200, verbose_name="Имя клиента")
    phone = models.DecimalField(
        max_digits=10, decimal_places=2, verbose_name="Телефон клиента"
    )
    master = models.ForeignKey(Master, related_name="master", on_delete=models.CASCADE)
    service = models.ForeignKey(
        Service, related_name="services", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Клиента"
        verbose_name_plural = "Клиенты"
