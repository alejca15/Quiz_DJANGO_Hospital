from django.db import models
from django.core.exceptions import ValidationError

class Pacientes(models.Model):
    nombre_paciente = models.CharField(max_length=100)
    apellido_paciente = models.CharField(max_length=100)
    contacto =  models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_paciente
    
class Especialidades(models.Model):
    nombre_especialidad = models.CharField(max_length=100,unique=True)
    
    def __str__(self):
        return self.nombre_especialidad
    
class Sedes(models.Model):
    nombre_sede = models.CharField(max_length=100)
    ubicacion_sede = models.CharField(max_length=100)
    
    def __str__(self):
        return self.nombre_sede
    

class Medicos(models.Model):
    nombre_medico = models.CharField(max_length=100)
    apellido_medico=models.CharField(max_length=100)
    id_sede = models.ForeignKey(Sedes, on_delete=models.CASCADE)
    id_especialidad=models.ForeignKey(Especialidades, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nombre_doctor

class Citas(models.Model):
    fecha_cita = models.DateTimeField
    id_paciente = models.ForeignKey(Pacientes, on_delete=models.CASCADE)
    id_medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.id_paciente
    
    
    def clean(self):
        if Citas.objects.filter(fecha_cita=self.fecha_cita, id_medico=self.id_medico).exists():
            raise ValidationError(f'El médico {self.id_medico} ya tiene una cita programada a las {self.fecha_cita}.')
        if Citas.objects.filter(fecha_cita=self.fecha_cita, id_paciente=self.id_paciente).exists():
            raise ValidationError(f'El paciente {self.id_paciente} ya tiene una cita programada a las {self.fecha_cita}.')
        
    def save(self, *args, **kwargs):
        self.clean() 
        super(Citas, self).save(*args, **kwargs)


