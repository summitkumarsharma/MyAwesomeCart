from django.contrib import admin
from django.urls import path

from .import views

urlpatterns = [
  path("",views.index, name="shopHome"),
  path("about/",views.about, name="About Us"),
  path("services/",views.services, name="services"),
  path("contact/",views.contact, name="contact"),
  path("tracker/",views.tracker, name="Tracker"),
  path("productview/<int:myid>",views.productview, name="ProductView"),
  path("search/",views.search, name="Search"),
  path("checkout/",views.checkout, name="Checkout")
]