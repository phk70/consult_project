from django.contrib import admin
from .models import Master, Service


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    search_fields = ('first_name', 'last_name')
    list_filter = ('services',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'price',)
    search_fields = ('name',)
    filter_horizontal = ('name',)