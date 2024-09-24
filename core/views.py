from django.shortcuts import render, redirect

from .models import Master, Visit, Service
from .forms import VisitModelForm
from django.http import JsonResponse
from django.views.generic import View # Импорт базового View класса


MENU = [
        {'title': 'Главная', 'url': '/', 'active': True},
        {'title': 'Мастера', 'url': '#masters', 'active': True},
        {'title': 'Услуги', 'url': '#services', 'active': True},
        {'title': 'Отзывы', 'url': '#reviews', 'active': True},
        {'title': 'Запись на стрижку', 'url': '#orderForm', 'active': True},
    ]

def get_menu_context(menu: list[dict] = MENU):
    return {"menu": menu}

def main_page(request):

    masters = Master.objects.all()  # Добываем всех мастеров и помещаем в переменную для отображения на странице. ХЗ почему подчеркивается, все работает.
    menu = get_menu_context()

    if request.method == "POST":
        form = VisitModelForm(request.POST)
        if form.is_valid():            
            form.save()  # Создание и сохранение записи в модели Visit                       
            return redirect('thanks')  # Перенаправляем пользователя на страницу с благодарностью после успешного сохранения
        
        if form.errors:  # Если что - отдааем заполненную форму с ошибкой
            return render(request, "main.html", {"form": form, 'masters': masters, **menu})
    else:
        form = VisitModelForm()
    
    return render(request, 'main.html', {'form': form, 'masters': masters, **menu})


class ThanksView(View):
    
    def get(self, request):
        return render(request, "thanks.html", get_menu_context())


def get_services_by_master(request, master_id):
    
    services = Master.objects.get(id=master_id).services.all()
    services_data = [{'id': service.id, 'name': service.name} for service in services]
    return JsonResponse({'services': services_data})
