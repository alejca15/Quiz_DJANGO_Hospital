from django.db import models

class Pacientes(models.Model):
    nombre_paciente = models.CharField(max_length=100)
    apellido_paciente = models.CharField(max_length=100)
    contacto =  models.CharField(max_length=100)

    def __str__(self):
        return self.nombre