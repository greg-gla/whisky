from django.urls import path
<<<<<<< HEAD
from rango import views

app_name = 'pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('ChoosingDistillery/', views.ChoosingDistillery, name='ChoosingDistillery'),
=======
from pages import views

app_name = 'whisky'

urlpatterns = [
    path('', views.IndexView, name='index'),
    path('register/', views.regist, name='register'),
    path('login/', views.user_login, name='login'),
    # path('logout/', views.user_logout, name='logout'),

>>>>>>> 6bb36b44342b26eca9ab5972ca2a9ed2e8744a26
]
