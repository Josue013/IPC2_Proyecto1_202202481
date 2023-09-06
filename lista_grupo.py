from nodo_grupo import nodo_grupo

class lista_grupo:
    def __init__(self):
        self.cabeza = None
        self.size = 1
        self.datos = ""

    def agregar_grupo(self, grupo):
        nuevo = nodo_grupo(grupo)
        if self.cabeza is None:
            self.cabeza = nuevo
            self.size += 1
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        actual.siguiente = nuevo
        self.size += 1

    def __iter__(self):
        self.actual = self.cabeza
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        else:
            dato_actual = self.actual
            self.actual = self.actual.siguiente
            return dato_actual   

    def obtener_size(self):
        return self.size

    def generar_grafica(self):
        texto = ""
        actual = self.cabeza

        sentinela = actual.grupo.grupo
        
        fila = False
        while actual != None:
            
            self.datos += actual.grupo.datos_grupo.generar_grafica(f"G = {actual.grupo.grupo} (t = {actual.grupo.tiempos})")
            actual = actual.siguiente
        texto += "\n"+self.datos+"\n"
        return texto             