inventario = []

# servicios.py
# Módulo que contiene las funciones para manejar el inventario

def agregar_producto(inventario, nombre, precio, cantidad):
    """
    Agrega un nuevo producto al inventario.
    
    Parámetros:
        inventario (list): Lista de diccionarios que representa el inventario
        nombre (str): Nombre del producto a agregar
        precio (float): Precio unitario del producto
        cantidad (int): Cantidad inicial en stock
    
    La función modifica la lista 'inventario' directamente.
    """
    producto = {
        "nombre":nombre.strip(),
        "precio":float(precio),
        "cantidad":int(cantidad)
    }
    inventario.append(producto)
    print(f"El producto  {nombre.strip()} ha sido agregado exitosamente!")

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
    
def mostrar_inventario(inventario):
    if not inventario:
        print("No hay productos registrados")
        return
    else:
        for producto in inventario:
            print(f"{producto['nombre']} {producto['precio']} {producto['cantidad']}")


    

def buscar_producto(inventario, nombre):
    """
    Busca un producto por nombre en el inventario.
    
    Parámetros:
        inventario (list): Lista de diccionarios con los productos
        nombre (str): Nombre del producto a buscar
    
    Retorna:
        dict: El diccionario completo del producto si se encuentra
        None: Si el producto no existe en el inventario
    """
    nombre_buscar = nombre.strip().lower()
    
    for producto in inventario:
        if producto["nombre"].strip().lower() == nombre_buscar:
            return producto
    
    return None

    

def actualizar_producto():

    print("")   

def eliminar_producto(inventario,nombre):

    
    producto = buscar_producto(inventario, nombre)

    if producto:
        inventario.remove(producto)
        return True

    return False
        
        
