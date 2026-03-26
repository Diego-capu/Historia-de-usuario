from servicios import agregar_producto,mostrar_producto,calcular_estadisticas,eliminar_producto


inventario = []

def menu_principal():
    while True:
        print("Menu principal")
        print("1.Agregar producto")
        print("2.Mostrar producto")
        print("3.Calcular estadisticas")
        print("Salir")
        option = int(input("Ingrese la opcion que desea realizar: "))

        if option == 1:
            agregar_producto()
    
           
        elif option == 2:
            mostrar_producto()
            
        elif option == 3:
            calcular_estadisticas()
            
        elif option == 4:
            eliminar_producto()
        

if __name__ == "__main__":
    menu_principal()
