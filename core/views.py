from django.shortcuts import render, redirect

from .models import Master, Service
from .forms import VisitModelForm
from django.http import JsonResponse


def main_page(request):
    masters = Master.objects.all()  # Добываем всех мастеров и помещаем в переменную. ХЗ почему подчеркивается, все работает.
    
    if request.method == "POST":
        form = VisitModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thanks_you_page")  # создаем объект Формы, проверяем на валидность. Если ок, то сохраняем и перенаправляем на "Спасибо". Если нет, то обратно на главную.
        if form.errors:
            return render(request, "main.html", {"form": form, 'masters': masters})
    else:
        form = VisitModelForm()
    
    return render(request, "main.html", {"masters": masters, "form": form})


def thanks_you_page(request):
    return render(request, "thanks.html")  # Просто перекидывает на мини страницу Спасибо.


def get_services_by_master(request, master_id):
    services = Master.objects.get(id=master_id).services.all()
    services_data = [{'id': service.id, 'name': service.name} for service in services]
    return JsonResponse({'services': services_data})
