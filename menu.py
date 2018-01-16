#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os

def main():
    opcion = 0
    #OPCIONES
    os.system('clear')
    print("Selecciona una opción")
    print("\t opción 0: Media de retraso")
    print("\t opción 1: Probabilidad de retraso")
    print("\t opción 2: Probabilidad de cancelacion")
    print("\t opción 3: Probabilidad de cancelacion por causa")
    print("\t opción 4: Media de retraso en salida")
    print("\t opción 5: Probabilidad de retraso en salida")
    print("\t opción 6: Media de retraso en salida (solo vuelos retrasados)")
    print("\t opción 7: Media de retraso en llegada")
    print("\t opción 8: Probabilidad de retraso en llegada")
    print("\t opción 9: Media de retraso en llegada (solo vuelos retrasados)")
    print("\t opción 10: Media de retraso por aerolinea")
    print("\t opción 11: Media de retraso por aerolinea (solo vuelos retrasados)")
    print("\t opción 12: Probabilidad de retraso por aerolinea")
    print("\t opción 13: Probabilidad de cancelacion por aerolinea")

    try:
        opcion = int(input())
    except NameError:
        print("Selecciona una opción del menú")

    if opcion == 0:
        print("Escribe el origen: ")
        origen = raw_input()
        print("Escribe el destino: ")
        destino = raw_input()
        os.system("spark-submit consultas.py 0 "+origen+" "+destino)
    elif opcion == 1:
        print("Escribe el origen: ")
        origen = raw_input()
        print("Escribe el destino: ")
        destino = raw_input()
        os.system("spark-submit consultas.py 1 "+origen+" "+destino)
    elif opcion == 2:
        print("Escribe el origen: ")
        origen = raw_input()
        print("Escribe el destino: ")
        destino = raw_input()
        os.system("spark-submit consultas.py 2 "+origen+" "+destino)
    elif opcion == 3:
        print("Escribe el origen: ")
        origen = raw_input()
        print("Escribe el destino: ")
        destino = raw_input()
        os.system("spark-submit consultas.py 3 "+origen+" "+destino)
    elif opcion == 4:
        print("Escribe el origen: ")
        origen = raw_input()
        print("Escribe el destino: ")
        destino = raw_input()
        os.system("spark-submit consultas.py 4 "+origen+" "+destino)
    elif opcion == 5:
        print("Escribe el origen: ")
        origen = raw_input()
        print("Escribe el destino: ")
        destino = raw_input()
        os.system("spark-submit consultas.py 5 "+origen+" "+destino)
    elif opcion == 6:
        print("Escribe el origen: ")
        origen = raw_input()
        print("Escribe el destino: ")
        destino = raw_input()
        os.system("spark-submit consultas.py 6 "+origen+" "+destino)
    elif opcion == 7:
        print("Escribe el origen: ")
        origen = raw_input()
        print("Escribe el destino: ")
        destino = raw_input()
        os.system("spark-submit consultas.py 7 "+origen+" "+destino)
    elif opcion == 8:
        print("Escribe el origen: ")
        origen = raw_input()
        print("Escribe el destino: ")
        destino = raw_input()
        os.system("spark-submit consultas.py 8 "+origen+" "+destino)
    elif opcion == 9:
        print("Escribe el origen: ")
        origen = raw_input()
        print("Escribe el destino: ")
        destino = raw_input()
        os.system("spark-submit consultas.py 9 "+origen+" "+destino)
    elif opcion == 10:
        print("Escribe el origen: ")
        origen = raw_input()
        print("Escribe el destino: ")
        destino = raw_input()
        os.system("spark-submit consultas.py 10 "+origen+" "+destino)
    elif opcion == 11:
        print("Escribe el origen: ")
        origen = raw_input()
        print("Escribe el destino: ")
        destino = raw_input()
        os.system("spark-submit consultas.py 11 "+origen+" "+destino)
    elif opcion == 12:
        print("Escribe el origen: ")
        origen = raw_input()
        print("Escribe el destino: ")
        destino = raw_input()
        os.system("spark-submit consultas.py 12 "+origen+" "+destino)
    elif opcion == 13:
        print("Escribe el origen: ")
        origen = raw_input()
        print("Escribe el destino: ")
        destino = raw_input()
        os.system("spark-submit consultas.py 13 "+origen+" "+destino)

if __name__ == '__main__':
    main()

