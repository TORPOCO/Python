import json
import urllib.request

# Abrir conexión
respuesta = urllib.request.urlopen('http://globalmentoring.com.mx/api/clima.json')

#print(respuesta)
cuerpo_respuesta = respuesta.read()

json_respuesta = json.loads(cuerpo_respuesta.decode('utf-8'))
#print(json_respuesta)


#Ejercicio 1. Acceder al la lista clima
descripcion_clima = json_respuesta.get('clima')
print(descripcion_clima)

#Ejercicio 2. La lista clima se convierte a un uno objeto
descripcion_clima = json_respuesta.get('clima')[0]
print(descripcion_clima)


#Ejercicio 3. Acceder a la decripción del clima
descripcion_clima = json_respuesta.get('clima')[0].get('descripcion')
print(f'Descripción clima: {descripcion_clima}')


#Ejercicio 4. Acceder a la decripción del clima con otra sintaxis
descripcion_clima = json_respuesta['clima'][0]['descripcion']
print(f'Descripción clima con otra sintaxis: {descripcion_clima}')


#Ejercicio 5. Mostrar la temperatura minima y maxima
temp_min = json_respuesta.get('principal').get('temp_min')
print(f'Temperatura minima: {temp_min}')
temp_max = json_respuesta.get('principal').get('temp_max')
print(f'Temperatura máxima: {temp_max}')

