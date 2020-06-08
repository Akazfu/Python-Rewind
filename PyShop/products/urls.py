from django.urls import path
from . import views


# /Products
# /products/1/detail
urlpatterns = [
    path('', views.index),
    path('new/', views.new)
]