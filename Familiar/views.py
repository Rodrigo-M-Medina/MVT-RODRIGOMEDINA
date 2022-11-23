from django.shortcuts import render
from .models import Persona
from django.http import HttpResponse
from django.template import Template, Context
import datetime

def persona1(request):
    fecha=datetime.datetime.now()
    persona1=Persona(nombre="rodrigo",apellido="medina", edad=22, fecha=22/7/2022)
    persona2=Persona(nombre="Legolas",apellido="Hojaverde", edad=2931)
    persona3=Persona(nombre="frodo",apellido="bolson", edad=33)

    persona1.save()
    persona2.save()
    persona3.save()

    archivo=open("C:/Users/Anidem/Desktop/Condimento/mvtrodrigo/Familiar/Template/Template.html")
    template=Template(archivo.read())

    context=Context(
        {"nombre1": persona1.nombre, "apellido1": persona1.apellido, "edad1": persona1.edad, "fecha":fecha,
         "nombre2": persona2.nombre, "apellido2": persona2.apellido, "edad2": persona2.edad,
         "nombre3": persona3.nombre, "apellido3": persona3.apellido, "edad3": persona3.edad
            }
    )

    documento=template.render(context)
    return HttpResponse(documento)
