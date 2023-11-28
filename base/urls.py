from django.urls import path
from . import views 

urlpatterns = [
    
    path('', views.home, name="home"),
    path('blog/', views.art_works, name="art_works"),
    path('login/', views.login, name="login"),
    path('contact/', views.contact, name="contact"),
    path('account/', views.account, name="account"),
    path('artwork/', views.artwork, name="artwork"),

]