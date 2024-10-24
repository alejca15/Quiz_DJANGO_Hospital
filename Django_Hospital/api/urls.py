from django.urls import path
from . import views


urlpatterns = [
    path('pacientes/', views.PacientesListCreate.as_view(), name='producto-list'),
    path('pacientes/<int:pk>/', views.PacientesDetail.as_view(), name='producto-detail'),
    path('especialidades/', views.EspecialidadesListCreate.as_view(), name='Especialidades-list'),
    path('especialidades/<int:pk>/', views.EspecialidadesDetail.as_view(), name='Especialidades-detail'),
    path('sedes/', views.SedesListCreate.as_view(), name='Sedes-list'),
    path('sedes/<int:pk>/', views.SedesDetail.as_view(), name='Sedes-detail'),
    path('medicos/', views.MedicosListCreate.as_view(), name='Sedes-list'),
    path('medicos/<int:pk>/', views.MedicosDetail.as_view(), name='Sedes-detail'),
    path('citas/', views.CitasListCreate.as_view(), name='Citas-list'),
    path('citas/<int:pk>/', views.CitasDetail.as_view(), name='Citas-detail'),
]