from django.urls import path
from .import views
from .views import*
from django.conf import settings
from django.conf.urls.static import static
                                                         
urlpatterns=[
    path('',views.welcome, name='stand'),
    path('about-us',views.about, name='about'),
    path('blog',views.blog, name='blog'),
    path('digital-ikigega',views.Ikigega, name='ikigega'),
    path('digitalapp',views.digitalapp, name='digital'),
    path('registration/', views.registration, name='register'),
    path('<int:id>deleteInfos', views.delreg, name='deleteInfos'),
    path('<int:id>updateInfos', views.updatereg, name='updateInfos'),
    path('reg/endpoint', views.registerEndpoint, name='endpoint'),
    path('deleteEndpoints/<int:id>', views.deleteEndpoint, name='deleteEndpoints'),
    path('user-creation/', CustomAuthToken.as_view())
] + static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)