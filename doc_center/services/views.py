from django.shortcuts import render, redirect, reverse
from django.contrib.auth.decorators import login_required

from .forms import RequestForm
from .models import Service

# Create your views here.
def index(request):
    services = Service.objects.order_by("-id")
    return render(request, "services/index.html", {"services": services})

# new request
@login_required
def newRequest(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            service = form.save(commit=False)
            service.user = request.user
            service.save()
            return redirect(reverse("services:index"))
    else:
        form = RequestForm()
    return render(request, "services/new-request.html", {"form": form})
