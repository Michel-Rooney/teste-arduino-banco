from django.urls import path
from . import views

urlpatterns = [
    path('teste/<int:value>/', views.index, name='index'),
]