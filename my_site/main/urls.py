
from django.urls import path
from . import views

urlpatterns = [
    path('index.html',views.index),
    path('theme1.html', views.theme1),
    path('theme2.html', views.theme2),
    path('theme3.html', views.theme3),
    path('theme4.html', views.theme4),
    path('theme5.html', views.theme5)
]
