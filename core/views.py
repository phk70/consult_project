from django.shortcuts import render


def main_page(request):
    return render(request, "main.html")


def thanks_you_page(request):
    return render(request, "thanks.html")


def service_fetch(request):
    pass
