import subprocess
import os
import sqlite3

def limpiar_consola():
    subprocess.run('cls' if os.name == 'nt' else 'clear', shell=True)

def pausar():
    """funcion para evitar que limpiar_consola no limpie mensajes de error y tablas
    al instante hasta que el usuario no precione enter"""
    print ("-" * 44)
    input ("\nToca Enter para continuar...")


def agregar_productos(conexion):
    """agrega productos por nombre, categoria y precio"""
    cursor = conexion.cursor()
    print ("-" * 44)
    while True:                                             
        nombre = input ("\nNombre de Producto: ")
        if nombre.strip() == "":
            print ("\nNo puede ingresar un dato vacio")
        else:
            break
    while True:
        categoria = input ("\nIngrese una Categoria: ")
        if categoria.strip() == "":
            print ("\nNo puede ingresar un dato vacio")
        else:
            break
    while True:
        precio = input("\nIngrese un Precio: ")
        try:
            precio = float(precio)
            break
        except ValueError:
            print ("-" * 44)
            print ("\nEl dato ingresado no es valido")
    try: 
        cursor.execute(
                "INSERT INTO productos (producto, categoria, precio) VALUES (?,?,?)", (nombre.capitalize(), categoria.capitalize(), precio)
            )
        conexion.commit()
        print ("-" * 44)
        print("\nProducto agregado exitosamente")
    except sqlite3.Error as error:
        conexion.rollback()
        print (f"Ocurrio un error al guardar un producto {error}")
         

def mostrar_productos(conexion):
    """Muestra la tabla con todos los productos en la base de datos"""
    cursor = conexion.cursor()
    cursor.execute ("SELECT * FROM productos ORDER BY id")
    filas = cursor.fetchall()

    if not filas:
        print ("-" * 44)
        print ("\nNo hay productos cargados")
        return
    print ("\n===LISTA DE PRODUCTOS===")
    print (f"{'ID':<4}{'Producto':<15}{'Precio':>10}  {'Categoria':<15}")
    print ("-" * 44)
    for item in filas:
        print (f"{item[0]:<4}{item[1]:<15}{item[3]:>10.2f}  {item[2]:<15}")


def buscar_producto(conexion):
    """busca productos en base a su nombre"""
    cursor = conexion.cursor()
    print ("-" * 44)
    busqueda = input ("\nIntruduzca el producto a buscar: ").strip()
    if not busqueda:
        print("\nDebe ingresar un dato de busqueda")
        return
    cursor.execute(
        "SELECT * FROM productos WHERE producto LIKE ? ORDER BY id", (f"%{busqueda}%",)
    )
    filas = cursor.fetchall()
    if not filas:
        print("\nNo se encontraron productos con ese nombre.")
        return
    print ("\n===Resultados de Busqueda===")
    print(f"{'ID':<4}{'Producto':<15}{'Precio':>10}  {'Categoria':<15}")
    print("-" * 44)
    for item in filas:
        print(f"{item[0]:<4}{item[1]:<15}{item[3]:>10.2f}  {item[2]:<15}")


def eliminar_producto(conexion):
    """Elimina productos por id asignado en la lista"""
    print ("-" * 44)
    mostrar_productos(conexion)
    print ("-" * 44)

    try:
        borrar_id = int (input ("\nIntroduzca el ID del producto a eliminar: ").strip())
    except ValueError:
        print ("\nIngrese un ID valido")
        return
    
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM productos WHERE id = ?", (borrar_id,))
    producto = cursor.fetchone()

    if producto is None:
        print ("-" * 44)
        print ("\nEl producto con dicho ID no existe")
        return
    
    print (f"\nProducto encontrado: {producto[1]} - {producto[3]} - {producto[2]}")
    print ("-" * 44)
    confirmacion = input("\n¿Confirma que desea eliminarlo? (s/n): ")

    if confirmacion.lower() == "s":
        try:
            cursor.execute("DELETE FROM productos WHERE id = ?", (borrar_id,))
            conexion.commit()
            print ("\nProducto eliminado exitosamente")
        except sqlite3.Error as error:
            conexion.rollback()
            print (f"Ocurrio un error al eliminar el producto: {error}")
    else:
        print ("\nOperacion Cancelada")
