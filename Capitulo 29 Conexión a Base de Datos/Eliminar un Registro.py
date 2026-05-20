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
            sentencia = 'DELETE FROM persona WHERE id_persona=%s'
            entrada = input('Proporcioar el id_persona a eliminar: ')
            valores = (entrada,)
            cursor.execute(sentencia, valores)
            registros_eliminado = cursor.rowcount
            print(f'Registro eliminado: {registros_eliminado}')
except Exception as e:
 print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

