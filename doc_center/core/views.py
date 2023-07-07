from django.shortcuts import render, redirect, get_list_or_404
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from library.models import Book
from services.models import Service

# Create your views here.

# logged in user dashboard
@login_required
def index(request):
    documents = Book.objects.filter(issuing_officer = request.user, returned=False).all()
    services = Service.objects.filter(user = request.user).all()
    return render(request, "core/index.html", {"documents": documents, "services": services})


# logout user
def logout_user(request):
    logout(request)
    return redirect("library:index")
