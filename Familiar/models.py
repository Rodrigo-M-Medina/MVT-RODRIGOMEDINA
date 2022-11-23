from django.db import models
import datetime

class Persona(models.Model):
    nombre=models.CharField(max_length=50)#este es el str
    apellido=models.CharField(max_length=50)
    edad=models.IntegerField()
    fecha=datetime.datetime.today()

    def __str__(self):
        return self.nombre+" "+self.apellido+" "+self.edad
