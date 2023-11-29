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

]