list = []

start_programan = True

print("1.- insertar nuevo elemento a la lista")
print("2.- elminar elemento de la lista")
print("3.- listar toda la lista")

while start_programan:
    option = int(input("Ingresa tu opcion: "))
    if option == 1:
        data = input("insertar dato: ")
        list.append(data)
    elif option == 2:
        data = input("Eliminar elemento :")
        list.remove(data)
    elif option == 3:
        print(list)
