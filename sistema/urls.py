from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),  # ✔️ Llama a la función correcta
]
