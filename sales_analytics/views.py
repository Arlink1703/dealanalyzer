from collections import Counter

from django.db.models import Sum
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from upload_csv.models import Deal


class GetTopCustomers(ListAPIView):
    def get(self, request, *args, **kwargs):
        top_deals = (
            Deal.objects.values("customer")
            .annotate(spent_money=Sum("total"))
            .order_by("-spent_money")[:5]
        )

        if not top_deals:
            return render(request, "top_customers.html", {"top_customers": None})

        top_customers = []

        for deal in top_deals:
            customer = {
                "username": deal["customer"],
                "spent_money": deal["spent_money"],
                "gems": list(
                    Deal.objects.filter(customer=deal["customer"])
                    .values_list("item", flat=True)
                    .distinct()
                ),
            }
            top_customers.append(customer)

        gem_counts = Counter(
            gem for customer in top_customers for gem in customer["gems"]
        )
        common_gems = [gem for gem, count in gem_counts.items() if count >= 2]

        for customer in top_customers:
            customer["gems"] = [gem for gem in customer["gems"] if gem in common_gems]

        return render(request, "top_customers.html", {"top_customers": top_customers})
