from django import forms
from .models import Master, Service, Client


class ClientForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    phone = forms.CharField(max_length=15, required=True)
    master = forms.ModelChoiceField(
        queryset=Master.objects.all(), required=True, label="Выберите мастера"
    )
    service = forms.ModelChoiceField(
        queryset=Service.objects.none(), required=True, label="Выберите услугу"
    )
