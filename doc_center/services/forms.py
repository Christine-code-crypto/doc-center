from django import forms

from .models import Service

INPUT_CLASS = "w-full py-3 rounded-lg mb-2 mt-2"


class RequestForm(forms.ModelForm):
    class Meta:
        model = Service
        fields = ["title_of_document", "type", "department", "customers_name", "customers_signature", "no_of_pages", "quantity_rate", "total" ]
        widgets = {
            "title_of_document": forms.TextInput(attrs={"class": INPUT_CLASS}),
            "type": forms.Select(attrs={'class': INPUT_CLASS}),
            "department": forms.TextInput(attrs={"class": INPUT_CLASS}),
            "no_of_pages": forms.NumberInput(attrs={"class": INPUT_CLASS}),
            "quantity_rate": forms.NumberInput(attrs={"class": INPUT_CLASS}),
            "total": forms.NumberInput(attrs={"class": INPUT_CLASS}),
            "customers_name": forms.TextInput(attrs={"class": INPUT_CLASS}),
            "customers_signature": forms.TextInput(attrs={"class": INPUT_CLASS}),
        }