from django.conf import settings
from django.urls import path,include
from django.contrib import admin
from . import views
from django.conf.urls.static import static

urlpatterns = [
    path('signup/', views.index, name='index'),
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('account/', include('django.contrib.auth.urls')), 
    path('createpost/', views.createpost, name='createpost'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)