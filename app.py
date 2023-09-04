import os

class main:
    def __init__(self):
        pass

    def menu(self):
        print("=======================================")
        print("============ MENU PRINCIPAL ===========")
        print("=======================================")
        print("1. Cargar Archivo")
        print("2. Procesar Archivo")
        print("3. Escribir Archivo Salida") 
        print("4. Mostrar Datos del Estudiante")
        print("5. Generar Gráfica")
        print("6. Inicializar sistema")
        print("7. Salida") 
        opcion = input("Ingrese una opción: ")
        if opcion == "1":
            # Cargar Archivo
            self.menu()
        elif opcion == "2":
            # Procesar Archivo
            self.menu()
        elif opcion == "3":
            # Escribir Archivo Salida
            self.menu()
        elif opcion == "4":
            # Mostrar Datos del Estudiante
            print("=======================================")
            print("========== DATOS DEL ESTUDIANTE =======")
            print("=======================================")
            print("> Josué Nabí Hurtarte Pinto")
            print("> 202202481")
            print("> Introducción a la Programación y Computación 2 sección D")
            print("> Ingeniería en Ciencias y Sistemas")
            print("> 4to Semestre")
            self.menu()
        elif opcion == "5":
            # Generar Gráfica
            self.menu()
        elif opcion == "6":
            # Inicializar sistema
            self.menu()
        elif opcion == "7":
            # Salida
            self.menu()
        else:
            print("Opción no válida")


Iniciar = main()
Iniciar.menu()            