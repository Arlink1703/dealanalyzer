from django.forms import FileField, Form, ModelForm

from .models import Deal


class DealsUploadForm(ModelForm):
    class Meta:
        model = Deal
        fields = ["customer", "item", "total", "quantity", "date"]


class UploadForm(Form):
    deal_file = FileField()
