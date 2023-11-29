from django.urls import path
from . import views 

urlpatterns = [
    
    path('', views.home, name="home"),
    path('blog/', views.art_works, name="art_works"),
    path('login/', views.login, name="login"),
    path('maps/', views.maps, name="maps"),
    path('account/', views.account, name="account"),
    path('artwork/<str:pk>/', views.artwork, name="artwork"),
    path('post_comment/', views.post_comment, name="post_comment"),
    path('regist/', views.regist, name="regist"),
    path('addartwork/', views.addartwork, name="addartwork"),
    path('exhibition/', views.exhibition, name="exhibition"),
    path("liked_exhibition/", views.liked_exhibition, name="liked_exhibition"),
    path("unliked_exhibition/", views.unliked_exhibition, name="unliked_exhibition"),
    path("liked_artwork/", views.liked_artwork, name="liked_artwork"),
    path("unliked_artwork/", views.unliked_artwork, name="unliked_artwork"),

]