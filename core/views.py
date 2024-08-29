from django.shortcuts import render, redirect

from core.models import Master, Visit, Service
from .forms import VisitModelForm
from django.http import JsonResponse


def main_page(request):
    masters = Master.objects.all()
    
    if request.method == "POST":
        form = VisitModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thanks_you_page")
    else:
        form = VisitModelForm()
    return render(request, "main.html", {"masters": masters, "form": form})


def thanks_you_page(request):
    return render(request, "thanks.html")


def service_fetch(request):
    pass

def get_services_by_master(request, master_id):
    services = Master.objects.get(id=master_id).services.all()
    services_data = [{'id': service.id, 'name': service.name} for service in services]
    return JsonResponse({'services': services_data})
