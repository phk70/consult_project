from django.contrib import admin
from .models import Master, Service, Visit

# admin.site.register(Master)
# admin.site.register(Service)
# admin.site.register(Visit)


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ("name", "phone", "created_at", "status")  # Что будет отображаться в моделе
    list_filter = ("status", "created_at")  # фильтр по полям
    search_fields = ("name", "phone", "comment")


@admin.register(Master)
class MasterAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "photo")
    search_fields = ("first_name", "last_name")
    list_filter = ("services",)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ("name", "price",)
    search_fields = ("name",)
