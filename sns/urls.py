from django.contrib import admin
from django.urls import path, include   # include 추가
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('test/', views.base_response, name='first_test'),
    path('first/', views.first_view, name='first_view'),
    path('', include('user.urls')),     # user/urls.py 경로에 추가
]
