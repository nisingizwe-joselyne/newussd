from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.welcome, name='popschools'),
    path('about-us',views.about, name='about'),
    path('our-price',views.pricing, name='price'),
    path('digitalapp',views.digitalapp, name='digital')
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)