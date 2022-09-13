from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.Registration.as_view()),
    path('login/', views.Login.as_view())
]
