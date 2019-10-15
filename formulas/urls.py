from django.urls import path
from . import views

urlpatterns = [
    path('', views.formulas_index, name='formulas_index'),
    path('formulas/<int:pk>/', views.formula_detail, name='formula_detail'),
]
