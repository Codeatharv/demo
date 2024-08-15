
from django.urls import path 
from .import views


urlpatterns = [
path('file',views.FileCL.as_view(),name='file'),
path('file/<int:pk>',views.FileRUD.as_view(),name='file'),

]