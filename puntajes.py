#!/usr/bin/env python
# -*- coding: utf-8 -*-
from csv import * 
 
def guardar_puntajes(nombre_archivo, puntajes):
    archivo = open(nombre_archivo, "w")
    archivo_csv = writer(archivo)
    archivo_csv.writerows(puntajes)
    archivo.close()

def recuperar_puntajes(nombre_archivo):
    puntajes = []
    archivo = open(nombre_archivo, "r")
    archivo_csv = reader(archivo)
    for nombre, puntaje, tiempo in archivo_csv:
        puntajes.append((nombre, int(puntaje), tiempo))
    archivo.close()
    return puntajes

def imprimirPuntaje():
    recuperado = recuperar_puntajes("puntajes.txt")
    for i in range(len(recuperado)):
        for j in range(len(recuperado[i])):
            print " -> " , recuperado[i][j] , " " , 
        print 
