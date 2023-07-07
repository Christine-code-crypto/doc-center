from django import forms

from .models import Book

INPUT_CLASS = "w-full py-3 rounded-lg mb-3 mt-3"

class NewDocumentForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["author", "title", "no_of_volume", "date_borrowed", "due_back", "issued_to", "borrower_signature"]
        widgets = {
            "author": forms.TextInput(attrs={"class": INPUT_CLASS, "placeholder": "Author of the book"}),
            "title": forms.TextInput(attrs={"class": INPUT_CLASS, "placeholder": "Title of the book"}),
            "no_of_volume": forms.TextInput(attrs={"class": INPUT_CLASS, "placeholder": "Volume number"}),
            "date_borrowed": forms.DateInput(attrs={"class": INPUT_CLASS, "placeholder": "Title of the book", "type": "date"}),
            "due_back": forms.DateInput(attrs={"class": INPUT_CLASS, "placeholder": "Title of the book", "type": "date"}),
            "issued_to": forms.TextInput(attrs={"class": INPUT_CLASS, "placeholder": "Name of the borrower"}),
            "borrower_signature": forms.NumberInput(attrs={"class": INPUT_CLASS, "placeholder": "Borrower signature"}),
        }


# lend document to a user
class LendDocument(forms.ModelForm):
    class Meta:
        model = Book
        exclude = ["name", "categories", "description", "image", "created_by", "returned", "borrowed", "return_date", "issued_by"]
        widgets = {
            "issued_to": forms.TextInput(attrs={"class": INPUT_CLASS}),
            "return_date": forms.DateInput(attrs={"class": INPUT_CLASS})
        }

# return document
class ReturnBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = ["returned", "issued_to", "date_returned", "borrower_signature" ]
        widgets = {
            "returned": forms.CheckboxInput(attrs={"class": "w-8 h-8", "type": "checkbox"}),
            "issued_to": forms.TextInput(attrs={"class": INPUT_CLASS}),
            "date_returned": forms.DateInput(attrs={"class": INPUT_CLASS, "type": "date"}),
            "borrower_signature": forms.NumberInput(attrs={"class": INPUT_CLASS})
        }