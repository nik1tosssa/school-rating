
from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.index, name='main'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
]
