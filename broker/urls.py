from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('tarnsactionslist/', views.tarnsactionslist, name="tarnsactionslist"),
    path('create_transaction/', views.create_transaction, name="create_transaction"),
]
