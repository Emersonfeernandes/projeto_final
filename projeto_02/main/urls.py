from django.urls import path
from . import views

app_main = "main"
urlpatterns = [
    path('', views.home, name="home"),
    #path('', views.resultado, name='resultado'),
    #path('', views.Visual.as_view(), name='home')
]