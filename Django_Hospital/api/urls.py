from django.urls import path
from . import views


urlpatterns = [
    path('pacientes/', views.PacientesListCreate.as_view(), name='producto-list'),
    path('pacientes/<int:pk>/', views.PacientesDetail.as_view(), name='producto-detail'),
]