from django.urls import path
from realtime_app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('realtime/', views.realtime_page, name='realtime_page'),
     path('realtime_update/', views.realtime_update, name='realtime_update'),
]
