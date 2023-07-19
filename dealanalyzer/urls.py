from clear_csv.views import clear_table
from django.contrib import admin
from django.urls import path
from home.views import home, redirect_to_home
from upload_csv.views import UploadView
from sales_analytics.views import GetTopCustomers

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", redirect_to_home, name="redirect_to_home"),
    path("home/", home, name="home"),
    path("home/upload/", UploadView.as_view(), name="upload_deals"),
    path("delete", clear_table, name="delete"),
    path("home/top_customers/", GetTopCustomers.as_view(), name="get_top_customers"),
]
