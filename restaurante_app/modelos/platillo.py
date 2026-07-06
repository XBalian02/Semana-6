from modelos.producto import Producto

class Platillo(Producto):
    def __init__(self, nombre, precio, calorias, tiempo_prep):
        super().__init__(nombre, precio)
        self.calorias = calorias
        self.tiempo_prep = tiempo_prep

    def mostrar_informacion(self):
        return f"[Platillo] {super().mostrar_informacion()} | Calorías: {self.calorias}kcal | Tiempo: {self.tiempo_prep} min"