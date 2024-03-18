class Pared:
    def __init__(self, orientacion):
        self.orientacion = orientacion

class Ventana:
    def __init__(self, pared, superficie, proteccion):
        self.pared = pared
        self.superficie = superficie
        if proteccion is None:
            raise Exception("Protección obligatoria")
        self.proteccion = proteccion

class ParedCortina(Pared):
    def __init__(self, orientacion, superficie):
        super().__init__(orientacion)
        self.superficie = superficie

class Casa:
    def __init__(self, paredes):
        self.paredes = paredes
        self.ventanas = []

    def agregar_ventana(self, ventana):
        self.ventanas.append(ventana)

    def superficie_acristalada(self):
        total = 0
        for pared in self.paredes:
            if isinstance(pared, ParedCortina):
                total += pared.superficie
            else:
                for ventana in self.ventanas:
                    if ventana.pared == pared:
                        total += ventana.superficie
        return total

# Instanciación de las paredes
pared_norte = Pared("NORTE")
pared_oeste = Pared("OESTE")
pared_sur = Pared("SUR")
pared_este = Pared("ESTE")

# Instanciación de la casa con las 4 paredes
casa = Casa([pared_norte, pared_oeste, pared_sur, pared_este])

# Instanciación de las ventanas
try:
    ventana_norte = Ventana(pared_norte, 0.5, None)
except Exception as e:
    print(e)

try:
    ventana_norte = Ventana(pared_norte, 0.5, "Persiana")
except Exception as e:
    print(e)

ventana_oeste = Ventana(pared_oeste, 1, "Persiana")
ventana_sur = Ventana(pared_sur, 2, "Estor")
ventana_este = Ventana(pared_este, 1, "Cortina")

# Agregar las ventanas a la casa
casa.agregar_ventana(ventana_norte)
casa.agregar_ventana(ventana_oeste)
casa.agregar_ventana(ventana_sur)
casa.agregar_ventana(ventana_este)

print(casa.superficie_acristalada())  # Salida esperada: 4.5
