from conexion import crear_conexion
from funciones import limpiar_consola, agregar_productos, mostrar_productos, buscar_producto, eliminar_producto, pausar

def main():
    conexion = crear_conexion()

    #----Menu principal del sistema de gestion----

    while True:
        limpiar_consola()
        print ("\n----Sistema de Gestion Basica de Recursos----")
        print (f"\n1.Agregar producto \n2.Mostrar productos \n3.Buscar producto \n4.Eliminar producto \n5.Salir")
        try:
            opcion = int ( input ("\nIngrese el numero de la opcion deseada: "))
        except ValueError:
            print ("\nIngrese un numero valido")
            pausar()
            continue
        if opcion == 1:
            agregar_productos(conexion)
            pausar()
        elif opcion == 2:
            mostrar_productos(conexion)
            pausar()
        elif opcion == 3:
            buscar_producto(conexion)
            pausar()
        elif opcion == 4:
            eliminar_producto(conexion)
            pausar()
        elif opcion == 5:
            print ("\nCerrando el sistema...")
            break
        else:
            print ("-" * 25)
            print("\nOpcion invalida. Debe ser un numero del 1 al 5.")
            pausar()

    conexion.close()

if __name__ == "__main__":
    main()