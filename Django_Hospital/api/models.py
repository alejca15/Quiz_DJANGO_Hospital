from django.db import models

class Pacientes(models.Model):
    nombre_paciente = models.CharField(max_length=100)
    apellido_paciente = models.CharField(max_length=100)
    contacto =  models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    
class Especialidades(models.Model):
    nombre_especialidad = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
    
class Sedes(models.Model):
    nombre_sede = models.CharField(max_length=100)
    ubicacion_sede = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre
###
###
###
###
class Citas(models.Model):
    fecha_cita = models.DateField
    nombre_paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    nombre_medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre