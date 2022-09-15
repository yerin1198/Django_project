from django.urls import path, include
from . import views

urlpatterns = [
    path('signup/', views.Registration.as_view()),
    path('login/', views.Login.as_view()),
    path('uniquecheck/username', views.UsernameUniqueCheck.as_view(), name='uniquecheck_username'),
    path('uniquecheck/email', views.EmailUniqueCheck.as_view(), name='uniquecheck_email'),
]
