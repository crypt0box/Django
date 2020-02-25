from django.urls import path
from . import views

app_name = 'ThreeLineDiary'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.Login.as_view(), name='login'),
]