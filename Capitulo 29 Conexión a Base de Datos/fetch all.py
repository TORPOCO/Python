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

            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            entrada = input('Proporciona los id\'s a buscar (separado por comas): ')

            llaves_primarias = (tuple(entrada.split(',')),)
            #input nos da una cadena de texto "1,2,3"
            #split convierte a lista -> [1,2,3]
            #tuple convierte lista a tuplas(1,2,3)
            #lo envolvemos en otra tupla ((1,2,3),2 parametro nada) y lo enviamos
            #Para que el sql entienda que estamos enviando 1 parámetro y en el 2 no hay nada

            cursor.execute(sentencia, llaves_primarias)
            #cursor.execute('SELECT * FROM persona WHERE id_persona IN %s',((1,2,3),))

            registros = cursor.fetchall()
            for registro in registros:
                print(registro)
except Exception as e:
 print(f'Ocurrio un error: {e}')
finally:
    conexion.close()

