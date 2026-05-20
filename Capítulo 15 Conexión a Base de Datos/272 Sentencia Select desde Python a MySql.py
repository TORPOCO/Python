import mysql.connector

conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="personas_db"
)

#Crear objeto cursor
cursor = conexion.cursor()

#Ejecutamos la sentencia de tipo SELECT
cursor.execute("SELECT * FROM personas")

#Obtenemos los resultados con fetchall
resultado = cursor.fetchall()

for persona in resultado:
    print(persona)