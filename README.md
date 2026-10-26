Guía del Gestor de Inventario

¿De qué se trata este programa?

Este es un programa sencillo de consola desarrollado en Python. Está diseñado para ayudar a administrar los productos y el stock disponible en una tienda pequeña de forma fácil. Para organizar la información, utiliza dos listas paralelas (una para los nombres de los productos y otra para las cantidades), junto con ciclos y funciones.

¿Qué necesitas para usarlo?

Tener instalado Python 3 en tu computadora.
No hace falta instalar ninguna librería adicional o externa.

¿Cómo ponerlo a funcionar?

Donde guardaste el archivo y ejecutar el siguiente comando:
python main.py

¿Cómo se usa?

Al abrir el programa verás un menú principal en pantalla. Para elegir una opción, solo escribe el número correspondiente y presiona la tecla Enter.

Las opciones disponibles son estas:

Registrar un nuevo producto con su cantidad inicial.

Ver la lista completa del inventario.

Buscar un producto específico por su nombre.

Cambiar la cantidad disponible de un producto.

Eliminar un producto del sistema.

Ver cuántos productos distintos hay registrados.

Consultar cuál es el producto con mayor cantidad disponible.

Salir del programa.

Funciones implementadas

`mostrar_menu()`: imprime el menú.
`buscar_indice(nombre)`: devuelve la posición de un producto en la lista, o -1 si no existe.
`pedir_nombre()`: pide un nombre y no acepta textos vacíos.
`pedir_cantidad()`: pide una cantidad y no acepta valores negativos.
`registrar_producto()`: agrega un producto y su cantidad, evitando repetidos.
`mostrar_inventario()`: recorre las listas y muestra cada producto con su cantidad.
`buscar_producto()`: consulta un producto por nombre.
`modificar_cantidad()`: cambia la cantidad de un producto existente.
`eliminar_producto()`: elimina el producto de ambas listas.
`mostrar_resumen()`: muestra la cantidad de productos diferentes.
`mostrar_mayor_cantidad()`: muestra el producto (o productos) con más unidades.

Decisiones de diseño

Las dos listas siempre se modifican juntas: el producto en `productos[i]` corresponde a la cantidad en `cantidades[i]`.
No se permite registrar dos veces el mismo producto (sin importar mayúsculas o minúsculas); si ya existe, se sugiere usar la opción de modificar cantidad.
Antes de buscar, modificar o eliminar se verifica que el producto exista.

Limitaciones

Los datos solo viven mientras el programa está abierto; al cerrarlo se pierden.
