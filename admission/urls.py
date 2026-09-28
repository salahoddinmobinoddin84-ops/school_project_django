from django.urls import path
from . import views
urlpatterns = [
    path('', views.admission_view, name='admission'),
    path('status/', views.status_views, name='status'),
]