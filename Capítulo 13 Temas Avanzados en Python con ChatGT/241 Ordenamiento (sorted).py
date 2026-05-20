print('*** Ordenamiento e n Python ***')

# sintaxis: sorted(iterable, key=None , reverse=False)

empleados = ['Juan','Pedro','Maria']
#ordenar la lista
#empleados_ordenados = sorted(empleados, reverse=True)
empleados_ordenados = sorted(empleados)
print(f'Empleados ordenados:{empleados_ordenados}')

#Ordenar un diccinario (una llave)
empleados_dict = [
    {'nombre':'Juan','salario':3000},
    {'nombre':'Pedro','salario':3000},
    {'nombre':'Maria','salario':3000}
]

empleados_ordenados_por_salario = sorted(empleados_dict, key=lambda x: x['salario'])
print(f'Empleados ordenados por salario:{empleados_ordenados_por_salario}')