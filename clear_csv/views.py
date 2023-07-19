from django.shortcuts import redirect, render
from upload_csv.models import Deal


def clear_table(request):
    Deal.objects.all().delete()
    return redirect("home")

