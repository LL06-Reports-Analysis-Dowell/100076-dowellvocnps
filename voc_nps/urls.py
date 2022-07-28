from django.urls import path, include
from voc_nps import views

urlpatterns=[
    #path('',views.Login,name="login" ),
    path('',views.index,name = 'index'),
    path('home',views.home),
    path('preview',views.preview),
    path('brandurl',views.preview1),
    path('emcode',views.emcode),
    path('qrcode',views.qrGen),
    path('showqrcode',views.ShowQr),
    path('sendqr',views.SendMail),
    path('sendfeed',views.sendfeed),
    path('showvideo',views.ShowVideo),
    path('logout',views.logout,name="logout" ),


]