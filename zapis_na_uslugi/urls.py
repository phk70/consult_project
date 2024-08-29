from django.contrib import admin
from django.urls import path
from core.views import main_page, thanks_you_page, get_services_by_master
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_page, name="main_page"),
    path("thanks/", thanks_you_page, name="thanks_you_page"),
    path("get_services_by_master/<int:master_id>/", get_services_by_master, name="get_services_by_master"),
] 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
