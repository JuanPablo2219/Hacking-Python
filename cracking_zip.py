import zipfile

zip_filename = 'data.zip'
dictionary_filename = 'dictionary.txt'

zip_file = zipfile.ZipFile(zip_filename)

with open(dictionary_filename, 'r') as file:
    for line in file:
        password = line.strip()
        try:
            zip_file.extractall(pwd=password.encode('utf-8'))
            print(f"Archivo descomprimido con la contraseña: {password}")
            break  
        except (RuntimeError, zipfile.BadZipFile) as error:
            print(f"Contraseña incorrecta: {password}")
            


# import zipfile

# def extract_file(zfile, password):
#     try:
#         zfile.extractall(pwd=password.encode('utf-8'))
#         return password

#     except Exception as error:
#          print(error)

# def main():
#     zfile = zipfile.ZipFile('data.zip')
#     pass_file = open('dictionary.txt')

#     for _ in pass_file.readlines():
#         password = _.strip('\n')
#         guess = extract_file(zfile=zfile, password=password)

#         if(guess):
#             print(f'[+] Password {password} \n')
#             exit(0)


# if __name__ == "__main__":
#     main()












