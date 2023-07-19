from csv import DictReader
from io import TextIOWrapper

from django.shortcuts import render
from django.utils.html import strip_tags
from rest_framework.generics import ListCreateAPIView
from upload_csv.forms import DealsUploadForm, UploadForm
from upload_csv.models import Deal


class UploadView(ListCreateAPIView):
    def get(self, request, *args, **kwargs):
        return render(request, "upload.html", {"form": UploadForm()})

    def post(self, request, *args, **kwargs):
        Deal.objects.all().delete()

        deal_file = request.FILES.get("deal_file")

        if not deal_file:
            return render(request, "upload.html")

        rows = TextIOWrapper(deal_file, encoding="utf-8", newline="")
        row_count = 0
        error = None

        for row in DictReader(rows):
            row_count += 1

            if len(row) > len(Deal._meta.fields) - 1:
                error = "Было задано больше значений чем ожидалось."
                Deal.objects.all().delete()
                break

            if len(row) > len(Deal._meta.fields) - 1:
                error = "Было задано меньше значений чем ожидалось."
                Deal.objects.all().delete()
                break

            form = DealsUploadForm(row)
            if not form.is_valid():
                error = strip_tags(form.errors.as_ul())
                Deal.objects.all().delete()
                break
            form.save()

        return render(
            request,
            "upload.html",
            {
                "form": UploadForm(),
                "error": error[:-1] if error is not None else None,
                "row_count": row_count,
                "rows": rows,
            },
        )
