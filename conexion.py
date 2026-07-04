

import sqlite3
import os

def crear_conexion()-> sqlite3.Connection:
    carpeta_actual = os.path.dirname (os.path.abspath(__file__))
    ruta_db = os.path.join (carpeta_actual, "productos.db")

    conexion = sqlite3.connect(ruta_db)
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL
        )
    """)
    conexion.commit()
    return conexion