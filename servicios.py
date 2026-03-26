inventario = []


def agregar_producto():

    nombre =input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio del producto: "))
    cantidad = int(input("Ingrese la cantidad del producto: "))

    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print("Agregado exitosamente")
    return

def calcular_estadisticas():
    print("Estadistica inventario")
    if not inventario:
        print("")
    else:
        total_valor = sum(l['precio'] * l['cantidad'] for l in inventario)
        total_productos = len(inventario)

        print(f"valor total del inventario: ${total_valor}")
        print(f"cantidad de tipos de productos registrados: {total_productos} ")
        return
    
def mostrar_producto():
    if not inventario:
        print("")
    else:
        for l in (inventario):
            print(f"Nombre: {l['nombre']}, Precio: {l['precio']}, {l['cantidad']}")
            return