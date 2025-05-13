#Vamos a calcular el promedio de 'x' notas
suma_notas = 0
cantidad_notas = int(input('Ingrese la cantidad de notas: '))
for i in range(cantidad_notas):
    nota = float(input(f'Ingrese la nota {i + 1}: '))
    suma_notas += nota
promedio = suma_notas/cantidad_notas

print(f'El promedio de las notas ingresadas es {round(promedio,1)}')

#Listo, ahí tenemos el algoritmo.