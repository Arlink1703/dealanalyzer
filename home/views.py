from django.shortcuts import redirect, render
from rest_framework.decorators import api_view


@api_view(["GET"])
def redirect_to_home(request):
    return redirect("home")


@api_view(["GET"])
def home(request):
    return render(request, "home.html")
