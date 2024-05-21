import random

def adivina_el_numero():
    secret_number = random.randint(1,50)

    print("He escogido un número entre 1 y 50. ¿Puedes adivinar cuál es?")

    while True:
        intento = int(input("Introduce tu intento: "))

        if intento < secret_number:
            print("Demasiado bajo.")
        elif intento > secret_number:
            print("Demasiado alto.")
        else:
            print("¡Felicidades! Has adivinado el número.")
            break

adivina_el_numero()
