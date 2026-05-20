import mysql.connector

# Conexión a la base de datos
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="admin",
    database="personas_db"
)


cursor = conexion.cursor()

# Definir la consulta INSERT
sql = "INSERT INTO personas (nombre,apellido,edad) VALUES (%s, %s, %s)"

#Valores a insert
valores = ("Juan", "Perez",34)

#Ejecutar la consulta INSERT
cursor.execute(sql, valores)

# Confirmar cambios
conexion.commit()

print("Registro insertado correctamente")
print("ID insertado:", cursor.lastrowid)
print(f'Se ha agregado el nuevo registro a la bd : {valores}')

# Cerrar el cursor y la conexión
cursor.close()
conexion.close()

