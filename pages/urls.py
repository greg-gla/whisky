from django.urls import path
from rango import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('ChoosingDistillery/', views.ChoosingDistillery, name='ChoosingDistillery'),
]
