import psycopg2

conexion = psycopg2.connect(
    user="postgres",
    password="admin",
    host="127.0.0.1",
    port="5432",
    database="test_db"
)
try:
    with (conexion):
        with conexion.cursor() as cursor:
            sentencia = 'INSERT INTO persona (nombre,apellido,email) VALUES (%s,%s,%s)'
            valores = (
                ('Marcos', 'Cantu', 'Marcos@gmail.com'),
                ('Angel', 'Quintana', 'Angel@gmail.com'),
                ('Maria', 'Gonzales', 'Maria@gmail.com'),
            )
            cursor.executemany(sentencia, valores)
            registros_insertados = cursor.rowcount
            print(f'Registro insertados: {registros_insertados}')
except Exception as e:
 print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

