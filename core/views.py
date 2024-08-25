from django.shortcuts import render

from core.models import Master


def main_page(request):
    masters = Master.objects.all()
    return render(request, "main.html", {'masters': masters})


def thanks_you_page(request):
    return render(request, "thanks.html")


def service_fetch(request):
    pass
