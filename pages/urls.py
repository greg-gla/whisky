from django.urls import path
from pages import views

app_name = 'whisky'

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),

]
