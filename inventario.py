# Este bucle while True crea un programa que se ejecuta indefinidamente
while True:
    # El bloque try-except se usa para manejar errores de entrada
    try:
        # Solicitamos el nombre del producto, precio y cantidad
        nombre = input("Ingrese su nombre: ")
        precio = float(input("Ingrese su precio: "))
        cantidad = int(input("Ingrese la cantidad: "))

       # Realizamos el cálculo principal: precio unitario × cantidad
        costo_total = precio * cantidad

        # Mostramos todos los datos de forma clara 
        print(f"Nombre del producto: {nombre}")
        print(f"Precio del producto: {precio}")
        print(f"Cantidad del producto: {cantidad}")
        print(f"Costo total: {costo_total}")



    except ValueError as  e:
        print("Valor invalido")
