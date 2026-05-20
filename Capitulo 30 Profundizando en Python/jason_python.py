#Leer archivo jso
# JSON = JavaScript Object Notation
#importamos para
import json

# Se usa para hacer solicitudes a páginas web, descargar archivos o leer contenido desde una URL.
import  urllib.request


respuesta = urllib.request.urlopen("http://globalmentoring.com.mx/api/personas.json")
print(respuesta)

cuerpo_respuesta = respuesta.read()
print(cuerpo_respuesta)

#Procesamos la respuesta
json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
print(json_respuesta)

for persona in json_respuesta['personas']:
    print(f'Persona:{persona["nombre"]}{persona["edad"]}')

print(f'Total de personas: {(json_respuesta["total"])}')