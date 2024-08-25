from django.contrib import admin
from django.urls import path
from core.views import main_page, thanks_you_page


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main_page, name="main_page"),
    path("thanks/", thanks_you_page, name="thanks_you_page"),
]
