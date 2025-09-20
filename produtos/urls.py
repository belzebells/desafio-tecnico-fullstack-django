from django.urls import path
from ..desafio import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),
]
