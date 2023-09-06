from nodo_patron import nodo_patron

class lista_patron:
    def __init__(self):
        self.cabeza = None
        self.size = 1

    def insertar_patron(self, dato_patron):
        nuevo = nodo_patron(dato_patron = dato_patron)
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
            dato_actual = self.actual.dato_patron
            self.actual = self.actual.siguiente
            return dato_actual

    def obtener_size(self):
        return self.size        