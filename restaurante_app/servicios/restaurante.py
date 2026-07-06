class Restaurante:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def mostrar_menu(self):
        print("\n--- Menú del Restaurante Cocoa :3 ---")
        for p in self.productos:
            print(p.mostrar_informacion())
            