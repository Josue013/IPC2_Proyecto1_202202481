import os.path as path
from lista_datos import lista_datos
import Archivo as ar

class Archivo:
    def __init__(self, archivo):
        self.archivo = archivo
    def set_archivo(self, archivo):
        self.archivo = archivo
    def get_archivo(self):
        return self.archivo

def opcion_graficar():
    nombre = input("Ingrese el nombre de la señal a graficar: \n")
    if ar.validar_nombre_senal(nombre) == False:
        print("No existe la señal que ingresaste")
    else:
        print("Elige el tipo de gráfica que deseas generar: \n")
        print("1. Original")
        print("2. Patrones")
        print("3. Reducida")
        opcion_grafica = input("Ingrese una opcion: \n")

        if opcion_grafica == "1":
            print("")
            print("Generando la grafica... \n")
            nombre_archivo = input("Ingrese el nombre de la grafica: ")
            print("")
            ar.generar_grafica_original(nombre,nombre_archivo)
        
        elif opcion_grafica == "2":
            print("")
            print("Generando Grafica...")
            print("")
            nombre_archivo = input("Ingrese el nombre de la grafica: ")
            print("")
            ar.generar_grafica_patrones(nombre, nombre_archivo)

        elif opcion_grafica == "3":
            print("")
            print("Generando grafica...")
            print("")
            nombre_archivo = input("Ingrese el nombre de la grafica: ")
            print("")
            ar.generar_grafica_reducida(nombre, nombre_archivo)
            
        else:
            print("Opcion invalida")
            opcion_graficar()


archivo = Archivo("")            
class main:


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
            nombre = input("Ingrese el nombre del archivo: ")
            archivo.set_archivo(nombre)
            archivo_path = archivo.get_archivo() + ".xml"
            if not path.exists(archivo_path):
                archivo.set_archivo("")
                print("No se ha encontrado el archivo")
            else:
                try:
                    print("\nSe cargó el archivo con exito")
                    self.menu()
                except Exception as e:
                    print(f"Error: {e}")
                    self.menu()

            
        elif opcion == "2":
            # Procesar Archivo
            if archivo.get_archivo() != "":
                ar.leer_xml(archivo.get_archivo())
            else:
                print("Debe cargar un archivo primero")
            self.menu()
        elif opcion == "3":
            # Escribir Archivo Salida
            if archivo.get_archivo() != "":
                nombre_archivo = input("Ingrese el nombre que desea poner al archivo: \n")
                ar.generar_xml(nombre_archivo)
            else:
                print("Debe cargar un archivo primero")
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
            if archivo.get_archivo() != "":
                if ar.get_size_senales() > 0:

                    opcion_graficar()
                else:
                    print("Debes procesar el archivo primero")
            else:
                print("Primero debes cargar un archivo")
            self.menu()
        elif opcion == "6":
            # Inicializar sistema
            print("Se ha inicializado el sistema")
            ar.limpiar_datos()
            archivo.set_archivo("")
            self.menu()
        elif opcion == "7":
            # Salida
            print("Programa finalizado")
        else:
            print("Opción no válida")
            self.menu()


Iniciar = main()
Iniciar.menu()            