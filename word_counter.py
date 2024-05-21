def contador_palabras(cadena):
    palabras = cadena.split()
    return len(palabras)

cadena = 'Hello World Bye good'
numero_palabras = contador_palabras(cadena)
print(f'Numero de Palabras: {numero_palabras}')