import os

# Directorios de entrada y salida
directorio_entrada = 'directorio-de-entrada'
directorio_salida = 'directorio-de-salida'

# Nombre del archivo de salida
archivo_salida = 'merged.txt'

# Ruta completa del archivo de salida
ruta_salida = os.path.join(directorio_salida, archivo_salida)

# Lista para almacenar el contenido de todos los archivos
contenido_total = []

# Asegurarse de que el directorio de salida existe
os.makedirs(directorio_salida, exist_ok=True)

# Recorrer todos los archivos en el directorio de entrada
for filename in os.listdir(directorio_entrada):
    if filename.endswith('.txt'):  # Asegurarse de que solo se procesen archivos .txt
        filepath = os.path.join(directorio_entrada, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            contenido = f.read()
            contenido_total.append(contenido)

# Escribir todo el contenido en el archivo de salida
with open(ruta_salida, 'w', encoding='utf-8') as f:
    f.write('\n'.join(contenido_total))

print(f"Los archivos han sido unidos en '{ruta_salida}'")
