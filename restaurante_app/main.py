from modelos.platillo import Platillo
from modelos.bebida import Bebida
from servicios.restaurante import Restaurante

mi_restaurante = Restaurante()

p1 = Platillo("Sopa de macaco", 15.0, 600, 20)
p2 = Platillo("Arroz relleno", 12.5, 400, 15)
b1 = Bebida("Colada Morada", 2.5, 500)
b2 = Bebida("CocaCola", 1.5, 350)

mi_restaurante.agregar_producto(p1)
mi_restaurante.agregar_producto(p2)
mi_restaurante.agregar_producto(b1)
mi_restaurante.agregar_producto(b2)

mi_restaurante.mostrar_menu()