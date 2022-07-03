from django.shortcuts import render
from MiFamilia.models import Familia
from django.http import HttpResponse
from django.template import Context, Template, loader


# Create your views here.


def familiar1(self):

    familiar1 = Familia(nombre= "Pamela", apellido= "Botello", fecha_de_nacimiento= "1981-05-01", edad= 41)

    #familiar1.save()

    diccionario= {'nombre': familiar1.nombre, 'apellido': familiar1.apellido, 'fecha': familiar1.fecha_de_nacimiento, 'edad': familiar1.edad, 'titulo': "Familiar 1"}

    plantilla= loader.get_template('template1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)

    #texto1= f"Se agrego un nuevo familiar: {familiar1.nombre} {familiar1.apellido} Con fecha de nacimiento: {familiar1.fecha_de_nacimiento} y edad: {familiar1.edad}"
    #return HttpResponse(texto1)

def familiar2(self):

    familiar2 = Familia(nombre= 'Azul', apellido= "Fiorini", fecha_de_nacimiento= "1999-12-09", edad= 22)

    #familiar2.save()
    
    diccionario= {'nombre': familiar2.nombre, 'apellido': familiar2.apellido, 'fecha': familiar2.fecha_de_nacimiento, 'edad': familiar2.edad,'titulo': "Familiar 2"}

    plantilla= loader.get_template('template1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
    
    #texto2= f"Se agrego un nuevo familiar: {familiar2.nombre} {familiar2.apellido} Con fecha de nacimiento: {familiar2.fecha_de_nacimiento} y edad: {familiar2.edad}"
    #return HttpResponse(texto2)

def familiar3(self):

    familiar3 = Familia(nombre= "Pablo", apellido= "Fiorini", edad= 11, fecha_de_nacimiento= "2010-10-31")

    #familiar3.save()

    diccionario= {'nombre': familiar3.nombre, 'apellido': familiar3.apellido, 'fecha': familiar3.fecha_de_nacimiento, 'edad': familiar3.edad, 'titulo': "Familiar 3"}

    plantilla= loader.get_template('template1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
    
    #texto3= f"Se agrego un nuevo familiar: {familiar3.nombre} {familiar3.apellido} Con fecha de nacimiento: {familiar3.fecha_de_nacimiento} y edad: {familiar3.edad}"
    #return HttpResponse(texto3)

def familiar4(self):

    familiar4 = Familia(nombre= "Veronica", apellido= "Fiorini", edad= 7, fecha_de_nacimiento= "2014-12-09")

    #familiar4.save()

    diccionario= {'nombre': familiar4.nombre, 'apellido': familiar4.apellido, 'fecha': familiar4.fecha_de_nacimiento, 'edad': familiar4.edad, 'titulo': "Familiar 4"}

    plantilla= loader.get_template('template1.html')

    documento = plantilla.render(diccionario)

    return HttpResponse(documento)
    
    
    # texto4= f"Se agrego un nuevo familiar: {familiar4.nombre} {familiar4.apellido} Con fecha de nacimiento: {familiar4.fecha_de_nacimiento} y edad: {familiar4.edad}"
    # return HttpResponse(texto4)




    
