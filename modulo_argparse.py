import argparse

parser = argparse.ArgumentParser(description='descripcion del programa')
parser  .add_argument('archivo', type=str, help='Nombre del archivo a procesar')
parser  .add_argument('--mode', choices=['lectura', 'escritura'], default='lectura', help='Modo de operacion')
args = parser.parse_args()

print('Archivo', {args.archivo})
print('Modo', {args.modo})