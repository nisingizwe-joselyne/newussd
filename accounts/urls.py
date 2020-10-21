from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('regist', views.regist, name='regist'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout')
    ]