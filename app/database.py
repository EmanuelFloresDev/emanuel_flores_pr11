import mysql.connector
from mysql.connector import Error


def obtener_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            port=3308,
            user="root",
            password="123456",
            database="nutrilacteos"
        )

        if conexion.is_connected():
            print("Conexión a MySQL exitosa")
            return conexion

    except Error as e:
        print(f"Error de conexión a MySQL: {e}")

    return None