from django.shortcuts import render, redirect
from .models import Master, Visit, Service
from .forms import VisitModelForm, VisitEditModelForm
from django.http import JsonResponse
from django.views.generic import (
    View,
    TemplateView,
    FormView,
    CreateView,
    DetailView,
    UpdateView,
    ListView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


MENU = [
        {'title': 'Главная', 'url': '/', 'active': True},
        {'title': 'Мастера', 'url': '#masters', 'active': True},
        {'title': 'Услуги', 'url': '#services', 'active': True},
        {'title': 'Отзывы', 'url': '#reviews', 'active': True},
        {'title': 'Запись на стрижку', 'url': '#orderForm', 'active': True},
    ]

def get_menu_context(menu: list[dict] = MENU):
    return {"menu": menu}

class MainView(View):
    """
    Метод get - отвечает за запросы GET
    Есть еще и другие методы, например post, put, delete и т.д.
    """
    
    def get(self, request):
        menu = get_menu_context()
        form = VisitModelForm()
        masters = Master.objects.all()

        return render(request, "main.html", {"form": form, "masters": masters, **menu})
    

    def post(self, request):
        form = VisitModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("thanks")

        # Отдаем заполненную форму с ошибку
        if form.errors:
            return render(
                request,
                "main.html",
                {"form": form, "masters": Master.objects.all(), **get_menu_context()},
            )


class ServicesByMasterView(View):
    
    def get(self, request, master_id):
        services = Master.objects.get(id=master_id).services.all()
        services_data = [
            {"id": service.id, "name": service.name} for service in services
        ]
        return JsonResponse({"services": services_data})


class ThanksTemplateView(TemplateView):
    template_name = "thanks.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update(get_menu_context())
        return context


# VisitFormView

class VisitFormView(FormView):
    template_name = "visit_form.html"
    form_class = VisitModelForm
    success_url = "/thanks/"
    context = get_menu_context()

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class VisitCreateView(CreateView):
    template_name = "visit_form.html"
    model = Visit
    # fields = ["name", "phone", "comment", "master", "services"] # Мы можем обойтись даже без формы!!!
    form_class = VisitModelForm
    # Подтянем url по псевдониму thanks\
    # Функция для поиска маршрутов по имени
    success_url = reverse_lazy("thanks")
 
    
class VisitUpdateView(UpdateView):
    template_name = "visit_form.html"
    model = Visit
    # fields = ["name", "phone", "comment", "master", "services"] # Мы можем обойтись даже без формы!!!
    form_class = VisitEditModelForm
    # Подтянем url по псевдониму thanks\
    # Функция для поиска маршрутов по имени
    success_url = reverse_lazy("thanks")

    
class VisitDetailView(PermissionRequiredMixin, DetailView):
    permission_required = 'core.view_visit'
    # raise_exception = True
    template_name = "visit_detail.html"
    model = Visit
    context_object_name = "visit"


class VisitDeleteView(DeleteView):
    template_name = "visit_confirm_delete.html"
    model = Visit
    success_url = reverse_lazy("thanks")


class VisitListView(ListView):
    template_name = "visit_list.html"
    model = Visit
    context_object_name = "visits"
    paginate_by = 5

    def get_queryset(self):
        """
        Расширили служебный метод get_queryset()
        Который поставляет в контекст шаблона список записей
        """
        # Используя родителя получили все
        queryset = super().get_queryset()
        
        # Добыли поисковый запрос \ или None
        search_query = self.request.GET.get('search')
        
        # Если поисковый запрос есть, то фильтруем
        if search_query:
            queryset = queryset.filter(
                Q(name__icontains=search_query) | Q(phone__icontains=search_query)
            )
        return queryset
    
    def get_context_data(self, **kwargs):
        """
        Расширяем служебный метод get_context_data()
        Для передачи в контекст шаблона дополнительных данных
        касательно поисковой строки
        """
        context = super().get_context_data(**kwargs)
        search_query = self.request.GET.get('search')
        if search_query:
            context['search'] = search_query
        return context
    
    
@login_required
def protected_function_view(request):
    return render(request, 'protected.html', get_menu_context())

class ProtectedClassView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'protected.html', get_menu_context())
    

class Custom403View(TemplateView):
    template_name = '403.html'
    status_code = 403

class Custom404View(TemplateView):
    template_name = '404.html'
    status_code = 404