from django.shortcuts import render

from rest_framework import generics
from .models import Pacientes, Especialidades, Sedes, Citas
from .serializers import PacientesSerializer, EspecialidadesSerializer, SedesSerializer, CitasSerializer


# metodos productos


class PacientesListCreate(generics.ListCreateAPIView):
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer


class PacientesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer


class EspecialidadesListCreate(generics.ListCreateAPIView):
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer


class EspecialidadesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Especialidades.objects.all()
    serializer_class = EspecialidadesSerializer    


class SedesListCreate(generics.ListCreateAPIView):
    queryset = Sedes.objects.all()
    serializer_class = SedesSerializer


class SedesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Sedes.objects.all()
    serializer_class = SedesSerializer    
###
###
###
###
###
###
###
###
###
###
###


class CitasListCreate(generics.ListCreateAPIView):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer


class CitasDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Citas.objects.all()
    serializer_class = CitasSerializer   