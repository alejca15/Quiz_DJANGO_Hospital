from django.shortcuts import render

from rest_framework import generics
from .models import Pacientes
from .serializers import PacientesSerializer


# metodos productos


class PacientesListCreate(generics.ListCreateAPIView):
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer


class PacientesDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pacientes.objects.all()
    serializer_class = PacientesSerializer