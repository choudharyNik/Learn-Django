from django.urls import path
from BasicDjangoFunctionality import views

urlpatterns = [
    path('/', views.index),
    path('page1/', views.page1),
    path('random/', views.random),
    path('json/', views.jsonForm),
    path('json/jsonRes/', views.jsonResponse),
    path('getform/', views.GETform),
    path('getform/getredirect/', views.GETinfoDisplay),
    path('postform/', views.POSTform),
    path('postform/postredirect/', views.POSTinfoDisplay),
]