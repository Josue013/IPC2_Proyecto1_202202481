from nodo_dato_grupo import nodo_dato_grupo

class lista_DatoGrupo:
    def __init__(self):
        self.primero = None
        self.size = 0

    def insertar_dato_grupo(self, dato_grupo):
        nuevo_nodo = nodo_dato_grupo(dato_grupo = dato_grupo)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.size += 1
            return      
        actual = self.primero
        while actual.siguiente:
            actual = actual.siguiente        
        actual.siguiente = nuevo_nodo
        self.size += 1

    def __iter__(self):
        self.actual = self.primero
        return self

    def __next__(self):
        if self.actual is None:
            raise StopIteration
        else:
            dato_actual = self.actual.dato_grupo
            self.actual = self.actual.siguiente
            return dato_actual
        
    def obtener_size(self):
        return self.size
    
    def generar_grafica(self, grupo):
        datos = ""
        actual = self.primero
        sentinela = actual.dato_grupo.amplitud
        datos += f"""<TR><TD border="1" bgcolor="#ff455b">{grupo}</TD>"""
        
        fila = False
        while actual != None:
            if sentinela != actual.dato_grupo.amplitud:
                sentinela = actual.dato_grupo.amplitud
                fila = False
            if fila == False:
                fila = True
                datos += f"""<TD border="1" bgcolor="#3bebff">{str(actual.dato_grupo.valor)}</TD>\n"""
            else:
                datos += f"""<TD border="1" bgcolor="#3bebff">{str(actual.dato_grupo.valor)}</TD>\n"""        
            actual = actual.siguiente
        datos += """</TR>\n"""        
        return datos