from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.simplyLogin.as_view(), name='login'),

]