from modelos.producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, precio, volumen_ml):
        super().__init__(nombre, precio)
        self.volumen_ml = volumen_ml

    def mostrar_informacion(self):
        return f"[Bebida] {super().mostrar_informacion()} | Volumen: {self.volumen_ml}ml"