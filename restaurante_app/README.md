# Restaurante Cococa

## Descripción del Proyecto
Este sistema es una aplicación modular desarrollada en Python diseñada para gestionar el inventario de productos de un restaurante. Permite administrar tanto platillos como bebidas, aplicando los principios de la Programación Orientada a Objetos (POO) para garantizar un código organizado, escalable y mantenible.

## Estructura del Proyecto
├── restaurante_app/
│   ├── modelos/
│   │   ├── __init__.py
│   │   ├── producto.py
│   │   ├── platillo.py
│   │   └── bebida.py
│   ├── servicios/
│   │   ├── __init__.py
│   │   └── restaurante.py
│   └── main.py
└── README.md
## Principios de POO Aplicados
**Herencia**: Se implementó una clase padre `Producto` de la cual heredan `Platillo` y `Bebida`, reutilizando atributos comunes como el nombre y el precio a través de `super()`.
**Encapsulación**: El atributo `__precio` está protegido, impidiendo su modificación directa y permitiendo cambios únicamente a través de los métodos `obtener_precio()` y `cambiar_precio()`, los cuales incluyen validaciones para asegurar que el precio sea siempre positivo.
**Polimorfismo**: Se sobrescribió el método `mostrar_informacion()` en las clases hijas. Al recorrer la lista de productos, el sistema ejecuta la versión específica del método según el tipo de objeto (Platillo o Bebida), demostrando un comportamiento diferenciado.