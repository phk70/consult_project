from django.contrib import admin
from django.urls import path
from core.views import (
    ServicesByMasterView,
    MainView,
    ThanksTemplateView,
    VisitCreateView,
    VisitDetailView,
    VisitUpdateView,
    VisitDeleteView,
    VisitListView,
    protected_function_view,
    ProtectedClassView,
)
from django.conf.urls.static import static
from django.conf import settings
from user import urls
from django.conf.urls import include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", MainView.as_view(), name="main"),
    path("thanks/", ThanksTemplateView.as_view(), name="thanks"),
    path(
        "get_services_by_master/<int:master_id>/",
        ServicesByMasterView.as_view(),
        name="get_services_by_master",
    ),
    # CRUD для Visit
    path("visit/add/", VisitCreateView.as_view(), name="visit-form"),
    # Read на DetailView
    path("visit/<int:pk>/view/", VisitDetailView.as_view(), name="visit-view"),
    # Update на UpdateView
    path("visit/<int:pk>/edit/", VisitUpdateView.as_view(), name="visit-edit"),
    # DeleteView
    path("visit/<int:pk>/delete/", VisitDeleteView.as_view(), name="visit-delete"),
    # ListView
    path("visits/", VisitListView.as_view(), name="visits"),
    # Подключаем пользователей с префиксом user
    path("user/", include(urls)),
    # Тестовые урлы для проверки прав доступа
    path("protected-function/", protected_function_view, name="protected-function"),
    path("protected-class/", ProtectedClassView.as_view(), name="protected-class"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
