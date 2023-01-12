from django.urls import path
from BasicDjangoFunctionality import views

urlpatterns = [
    path('', views.index),
    path('getform/', views.GETform),
    path('getform/getredirect/', views.GETinfoDisplay),
    path('postform/', views.POSTform),
    path('postform/postredirect/', views.POSTinfoDisplay),
]