from django.contrib import admin
from django.urls import path
from core.views import main, thanks


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", main, name="main"),
    path("thanks/", thanks, name="thanks"),
]
