class Punto2D:  
    def __init__(self, x, y): 
        self.x = x 
        self.y = y 

    def traslacion(self, dx, dy):  # Método para realizar una traslación en 2D
        self.x += dx  # Incrementa la coordenada x por dx
        self.y += dy  # Incrementa la coordenada y por dy

    def __str__(self):  # Método para representar el objeto como string
        return "X: {}; Y: {}".format(self.x, self.y)  # Devuelve la representación como string del objeto


class Punto3D(Punto2D):  
    def __init__(self, x, y, z): 
        super().__init__(x, y)  
        self.z = z  

    def traslacion(self, dx, dy, dz):  # Método para realizar una traslación en 3D
        super().traslacion(dx, dy)  
        self.z += dz  # Incrementa la coordenada z por dz

    def __str__(self):  # Método para representar el objeto como string
        return "X: {}; Y: {}; Z: {}".format(self.x, self.y, self.z)  # Devuelve la representación como string del objeto


# Ejemplo de uso
a = Punto2D(1, 2)  # Crea un objeto Punto2D con coordenadas (1, 2)
print("A = {}".format(a))  # Imprime la representación de a como string
a.traslacion(-1, -2)  # Realiza una traslación de -1 en x y -2 en y
print("A = {}".format(a))  # Imprime la nueva representación de a como string

b = Punto2D(-3, 0)  # Crea un objeto Punto2D con coordenadas (-3, 0)
b.traslacion(5, -1)  # Realiza una traslación de 5 en x y -1 en y
print("B = {}".format(b))  # Imprime la representación de b como string

c = Punto3D(1, 2, 3)  # Crea un objeto Punto3D con coordenadas (1, 2, 3)
print("C = {}".format(c))  # Imprime la representación de c como string
c.traslacion(-1, -2, 1)  # Realiza una traslación de -1 en x, -2 en y y 1 en z
print("C = {}".format(c))  # Imprime la nueva representación de c como string
