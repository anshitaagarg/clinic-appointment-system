from django.urls import path
from . import views

urlpatterns = [
    path('queue/', views.queue_display, name='queue'),
    path('reports/', views.reports, name='reports'),
]