import random
import string

def generete_password(length: int):
    contraseña = ''
    for _ in range(length):
        index = random.randint(0, len(string.printable) -1)
        contraseña += string.printable[index]
    return contraseña.split(' \n')
print(generete_password(5))