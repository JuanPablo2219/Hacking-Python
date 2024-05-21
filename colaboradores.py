import string
import os

def mostrar_colaboradores (numero):
    with open('colaboradores.txt', 'r+') as archivo:
        print(archivo.readlines()[0: numero])

# mostrar_colaboradores();

def agg_colaboradores(nombre: string ):
    with open('colaboradores.txt' , 'a') as archivo:
        archivo.write(nombre)

init_programa = True

print('1.- mostrar colaboradores')
print('2.- agregar colaboradores')
print('3.- termianar programa')

while init_programa:
    opcion = int(input('Ingresa tu opcion : '))
    if opcion == 1:
        numero_colaboradores = (input('seleccione el numero de colaboradores a mostrar :'))
        colaboradores = mostrar_colaboradores(int(numero_colaboradores))

    elif opcion == 2:
        agregar = (input('Agrega nuevo colaborador :'))
        nuevo_colaborador = agg_colaboradores(agregar)

    elif opcion == 3:
        init_programa = False
        print('Fin del programa')
        os.system('clear') 
    
    
