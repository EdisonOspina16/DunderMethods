from dataclasses import dataclass


@dataclass
class Elemento:
    nombre: str

    def __eq__(self, other):
        if isinstance(other, Elemento):
            return self.nombre == other.nombre
        return False


class Conjunto:
    count = 0

    def __init__(self, nombre):
        self.__id = Conjunto.count
        self.elementos = []
        self.nombre = nombre
        Conjunto.count += 1

    def id(self):
        return self.__id

    def contiene(self, elemento):
        return any(elem.nombre == elemento.nombre for elem in self.elementos)

    def agregar_elemento(self, elemento):
        if not self.contiene(elemento):
            self.elementos.append(elemento)

    def unir(self, otro_conjunto):
        for elem in otro_conjunto.elementos:
            self.agregar_elemento(elem)

    def __add__(self, otro_conjunto):
        nuevo_conjunto = Conjunto(f"{self.nombre} UNIDO {otro_conjunto.nombre}")
        nuevo_conjunto.unir(self)
        nuevo_conjunto.unir(otro_conjunto)
        return nuevo_conjunto

    @classmethod
    def intersectar(cls, conjunto1, conjunto2):
        nombre_interseccion = f"{conjunto1.nombre} INTERSECTADO {conjunto2.nombre}"
        interseccion = Conjunto(nombre_interseccion)
        for elem in conjunto1.elementos:
            if conjunto2.contiene(elem):
                interseccion.agregar_elemento(elem)
                return interseccion

    def __str__(self):
        elementos_str = ', '.join(elem.nombre for elem in self.elementos)
        return f"Conjunto {self.nombre}: ({elementos_str})"


elemento1 = Elemento("A")
elemento2 = Elemento("B")
elemento3 = Elemento("C")

# Crear instancias de conjuntos
conjunto1 = Conjunto("Conjunto A")
conjunto2 = Conjunto("Conjunto B")

# Agregar elementos a los conjuntos
conjunto1.agregar_elemento(elemento1)
conjunto1.agregar_elemento(elemento2)

conjunto2.agregar_elemento(elemento2)
conjunto2.agregar_elemento(elemento3)

union = conjunto1 + conjunto2

interseccion = Conjunto.intersectar(conjunto1, conjunto2)


print("Conjunto 1:", conjunto1)
print("Conjunto 2:", conjunto2)
print("Unión de los conjuntos:", union)
print("Intersección de los conjuntos:", interseccion)
