from django.contrib import admin
from django.urls import path, include

from . import views
from .views import product

app_name = 'main'

urlpatterns = [
    path('product/', product, name='product'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product2/<int:pk>/', views.product2_detail, name='product2_detail'),

]