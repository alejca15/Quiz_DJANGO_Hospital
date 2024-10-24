from rest_framework import serializers
from .models import Pacientes, Especialidades, Sedes,Medicos,Citas

class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__'
        
class EspecialidadesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Especialidades
        fields = '__all__'
        
class SedesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sedes
        fields = '__all__'

class MedicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicos
        fields = '__all__'
        

class CitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citas
        fields = '__all__'