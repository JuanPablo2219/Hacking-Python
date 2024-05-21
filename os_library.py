import os
import shutil


try:
    os.mkdir("Backup")
except:
    print("La carpeta ya esta creada")

    files_extend = (".log", ".sql", ".key", ".pem")
    for root, dir, files in os.walk("."):
        for file in files:
            if file.endswith(".log"):
                shutil.copy(file, "Backup/" + file)
            if file.endswith(files_extend):
                print(os.path.join(root, file))
