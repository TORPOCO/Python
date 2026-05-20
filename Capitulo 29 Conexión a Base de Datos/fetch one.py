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
        with conexion.cursor() as cursor:#Abre el cursor automáticamente y lo cierra
            sentencia = 'SELECT * FROM persona WHERE id_persona = %s'
            id_persona = int(input("Proporciona el valor id_persona:"))
            cursor.execute(sentencia,(id_persona,))
            #fetchone() para regrese un registro
            registros = cursor.fetchone()
            print(registros)
except Exception as e:
 print(f'Ocurrio un error: {e}')
finally:
    # hay que cerrar manualmente el obj connect con la BD
    conexion.close()

