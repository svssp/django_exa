from . import views
from django.urls import path

urlpatterns = [
    path('', views.index,name='index'),
    path('newelement',views.newuser,name='newuser'),
    path('details',views.details,name='details')
]