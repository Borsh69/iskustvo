from django.urls import path
from . import views 

urlpatterns = [
    
    path('', views.home, name="home"),
    path('blog/', views.art_works, name="art_works"),
    path('login/', views.login, name="login"),
    path('contact/', views.contact, name="contact"),
    path('account/', views.account, name="account"),
    path('artwork/<str:pk>/', views.artwork, name="artwork"),
    path('post_comment/', views.post_comment, name="post_comment"),
    path('regist/', views.regist, name="regist"),
    path('addartwork/', views.addartwork, name="addartwork"),
    path('exhibition/', views.exhibition, name="exhibition"),
    path("liked/", views.liked, name="liked"),
    path("unliked/", views.unliked, name="unliked"),

]