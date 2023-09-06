from nodo import nodo
import os

class lista_datos:
    def __init__(self):
        self.primero=None
        self.ultimo=None
        self.size=0

    def agregar(self,Dato):
        nuevo=nodo(Dato)
        if self.primero is None: 
            self.primero=nuevo 
            self.ultimo=nuevo
        else:
            actual = self.primero
            anterior = None
            while actual is not None and (actual.dato.nombre_senal < nuevo.dato.nombre_senal or (actual.dato.nombre_senal == nuevo.dato.nombre_senal and (int(actual.dato.tiempo), int(actual.dato.amplitud)) < (int(nuevo.dato.tiempo), int(nuevo.dato.amplitud)))):
                anterior = actual
                actual = actual.siguiente
            if anterior is None:
                nuevo.siguiente = self.primero
                self.primero = nuevo
            else:
                nuevo.siguiente = actual
                anterior.siguiente = nuevo

        self.size += 1

    def __iter__(self):
        self.actual = self.primero
        return self  

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        else:
            dato_actual=self.actual
            self.actual=self.actual.siguiente
            return dato_actual     
        
    def generar_grafica(self,nombre,amplitud,tiempo,nombre_archivo):
        f = open('bb.dot','w')
        text ="""
            digraph G {"Amplitud="""+amplitud+"""","Tiempo="""+tiempo+""""->" """+nombre+ """" bgcolor="#bf4efc" style="filled"
            subgraph cluster1 {fillcolor="blue:red" style="filled"
            node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
        actual = self.primero
        sentinela_de_filas=actual.dato.tiempo 
        fila_iniciada=False
        while actual != None:
            if  sentinela_de_filas!=actual.dato.tiempo:
                sentinela_de_filas=actual.dato.tiempo
                fila_iniciada=False
                text+="""</TR>\n"""  
            if fila_iniciada==False:
                fila_iniciada=True
                text+="""<TR>"""  
                text+="""<TD border="3"  bgcolor="#fc8b49" gradientangle="315">"""+str(actual.dato.valor)+"""</TD>\n"""
            else:
                text+="""<TD border="3"  bgcolor="#fc8b49" gradientangle="315">"""+str(actual.dato.valor)+"""</TD>\n"""
            actual = actual.siguiente
        text+=""" </TR></TABLE>>];
                }
                }\n"""
        f.write(text)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f"dot -Tpng bb.dot -o {nombre_archivo}.png")
        print("Grafica creada exitosamente")  

    def generar_grafica_patrones(self, nombre_senal, tiempo, amplitud, nombre_grafica):
        f = open('bb.dot', 'w')

        texto = """
                digraph G {" """+nombre_senal+""""->"t = """+tiempo+"""";" """+nombre_senal+""""->"A = """+amplitud+"""" bgcolor="#bf4efc" style="filled"
            subgraph cluster1 {fillcolor="blue:red" style="filled"
            node [shape=circle fillcolor="gold:brown" style="radial" gradientangle=180]
            a0 [ label=<
            <TABLE border="10" cellspacing="10" cellpadding="10" style="rounded" bgcolor="blue:red" gradientangle="315">\n"""
            
        actual = self.primero
        sentinela = actual.dato.tiempo
        fila = False

        while actual != None:
            if sentinela != actual.dato.tiempo:
                sentinela = actual.dato.tiempo
                fila = False

                texto += """</TR>\n"""
            if fila == False:
                fila = True
                texto += """<TR>"""
                texto += """<TD border="3" style="solid" bgcolor="#fc8b49">"""+str(actual.dato.valor_binario)+"""</TD>\n"""
            else:
                texto += """<TD border="3" style="solid" bgcolor="#fc8b49">"""+str(actual.dato.valor_binario)+"""</TD>\n"""
            actual = actual.siguiente
        texto += """ </TR></TABLE>>];
                        }
                        }\n"""
        f.write(texto)
        f.close()
        os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin'
        os.system(f'dot -Tpng bb.dot -o {nombre_grafica}.png')
        print("Grafica creada exitosamente")  

