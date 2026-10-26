productos = []
cantidades = []


def mostrar_menu():
    print()
    print("===== GESTOR DE INVENTARIO =====")
    print("1. Registrar producto")
    print("2. Mostrar inventario")
    print("3. Buscar producto")
    print("4. Modificar cantidad")
    print("5. Eliminar producto")
    print("6. Mostrar cantidad de productos diferentes")
    print("7. Mostrar producto con mayor cantidad")
    print("8. Salir")


def buscar_indice(nombre):
    posicion = -1
    for i in range(len(productos)):
        if productos[i].lower() == nombre.lower():
            posicion = i
    return posicion


def pedir_nombre():
    nombre = input("Nombre del producto: ").strip()
    while nombre == "":
        print("El nombre no puede estar vacío.")
        nombre = input("Nombre del producto: ").strip()
    return nombre


def pedir_cantidad():
    cantidad = int(input("Cantidad disponible: "))
    while cantidad < 0:
        print("La cantidad no puede ser negativa.")
        cantidad = int(input("Cantidad disponible: "))
    return cantidad


def registrar_producto():
    nombre = pedir_nombre()
    if buscar_indice(nombre) != -1:
        print("Ese producto ya está registrado.")
        print("Use la opción 4 para modificar su cantidad.")
    else:
        cantidad = pedir_cantidad()
        productos.append(nombre)
        cantidades.append(cantidad)
        print("Producto registrado.")


def mostrar_inventario():
    if len(productos) == 0:
        print("El inventario está vacío.")
    else:
        print("--- INVENTARIO ---")
        for i in range(len(productos)):
            print(i + 1, productos[i], "-", cantidades[i])


def buscar_producto():
    if len(productos) == 0:
        print("El inventario está vacío.")
    else:
        nombre = pedir_nombre()
        posicion = buscar_indice(nombre)
        if posicion == -1:
            print("El producto no existe.")
        else:
            print("Producto encontrado:", productos[posicion])
            print("Cantidad disponible:", cantidades[posicion])


def modificar_cantidad():
    if len(productos) == 0:
        print("El inventario está vacío.")
    else:
        nombre = pedir_nombre()
        posicion = buscar_indice(nombre)
        if posicion == -1:
            print("El producto no existe.")
        else:
            print("Cantidad actual:", cantidades[posicion])
            nueva_cantidad = pedir_cantidad()
            cantidades[posicion] = nueva_cantidad
            print("Cantidad actualizada.")


def eliminar_producto():
    if len(productos) == 0:
        print("El inventario está vacío.")
    else:
        nombre = pedir_nombre()
        posicion = buscar_indice(nombre)
        if posicion == -1:
            print("El producto no existe.")
        else:
            productos.pop(posicion)
            cantidades.pop(posicion)
            print("Producto eliminado.")


def mostrar_resumen():
    print("Productos diferentes registrados:", len(productos))


def mostrar_mayor_cantidad():
    if len(productos) == 0:
        print("El inventario está vacío.")
    else:
        mayor = max(cantidades)
        print("Mayor cantidad disponible:", mayor)
        for i in range(len(productos)):
            if cantidades[i] == mayor:
                print("Producto:", productos[i])


opcion = 0

while opcion != 8:
    mostrar_menu()
    opcion = int(input("Seleccione una opción: "))

    if opcion == 1:
        registrar_producto()
    elif opcion == 2:
        mostrar_inventario()
    elif opcion == 3:
        buscar_producto()
    elif opcion == 4:
        modificar_cantidad()
    elif opcion == 5:
        eliminar_producto()
    elif opcion == 6:
        mostrar_resumen()
    elif opcion == 7:
        mostrar_mayor_cantidad()
    elif opcion == 8:
        print("Programa finalizado.")
    else:
        print("Opción inválida. Elija un número del 1 al 8.")
