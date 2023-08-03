from django.contrib import admin
from django.urls import path
from realtime_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('api/data/', views.data_api, name='data_api'),
    path('api/data/<int:id>/', views.data_detail_api, name='data_detail_api'),
    path('realtime/', views.realtime_page, name='realtime_page'),
    path('celery/', views.celery_demo, name='celery_demo'),
]
