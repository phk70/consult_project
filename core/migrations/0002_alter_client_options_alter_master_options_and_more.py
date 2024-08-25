# Generated by Django 5.1 on 2024-08-25 07:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Клиента', 'verbose_name_plural': 'Клиенты'},
        ),
        migrations.AlterModelOptions(
            name='master',
            options={'verbose_name': 'Мастера', 'verbose_name_plural': 'Мастера'},
        ),
        migrations.AlterModelOptions(
            name='service',
            options={'verbose_name': 'Услугу', 'verbose_name_plural': 'Услуги'},
        ),
        migrations.AlterField(
            model_name='master',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media/masters/photos/', verbose_name='Фото мастера'),
        ),
        migrations.AlterField(
            model_name='service',
            name='name',
            field=models.CharField(max_length=255, verbose_name='Наименование'),
        ),
        migrations.AlterField(
            model_name='service',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Цена'),
        ),
    ]
