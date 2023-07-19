from django.db import models


class Deal(models.Model):
    customer = models.CharField(max_length=255)
    item = models.CharField(max_length=255)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    date = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.customer} ({self.item})"

    class Meta:
        verbose_name = "Поле"
        verbose_name_plural = "Поля"
