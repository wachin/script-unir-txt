# script-unir-txt
Scirpt en python para unir varios archivos de texto en uno solo

**Requerimientos**
Python 

**Probado en**
MX Linux 21

**Explicación de funcionamiento de script:**

1. Importación de módulos:

```python
import os
```
Importamos el módulo `os` que nos permite interactuar con el sistema operativo, lo que es necesario para manejar directorios y archivos.

2. Definición de directorios y archivo de salida:

```python
directorio_entrada = 'directorio-de-entrada'
directorio_salida = 'directorio-de-salida'
archivo_salida = 'merged.txt'
ruta_salida = os.path.join(directorio_salida, archivo_salida)
```
Aquí definimos las rutas de los directorios de entrada y salida, el nombre del archivo de salida, y creamos la ruta completa del archivo de salida.

3. Inicialización de la lista para almacenar contenido:

```python
contenido_total = []
```
Esta lista almacenará el contenido de todos los archivos de texto.

4. Creación del directorio de salida:

```python
os.makedirs(directorio_salida, exist_ok=True)
```
Creamos el directorio de salida si no existe. `exist_ok=True` evita errores si el directorio ya existe.

5. Recorrido de archivos en el directorio de entrada:

```python
for filename in os.listdir(directorio_entrada):
    if filename.endswith('.txt'):
        filepath = os.path.join(directorio_entrada, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            contenido = f.read()
            contenido_total.append(contenido)
```
Este bucle recorre todos los archivos en el directorio de entrada, lee el contenido de cada archivo .txt y lo añade a la lista `contenido_total`.

6. Escritura del contenido en el archivo de salida:

```python
with open(ruta_salida, 'w', encoding='utf-8') as f:
    f.write('\n'.join(contenido_total))
```
Aquí abrimos el archivo de salida en modo escritura y escribimos todo el contenido almacenado, separando cada archivo con un salto de línea.

7. Mensaje de confirmación:

```python
print(f"Los archivos han sido unidos en '{ruta_salida}'")
```
Finalmente, imprimimos un mensaje indicando que el proceso se ha completado y dónde se ha guardado el archivo resultante.

Este script es eficiente para unir varios archivos de texto en uno solo, manteniendo una estructura organizada con directorios de entrada y salida separados.

**REFERENCIAS:**

1. Lutz, M. (2013). Learning Python (5th ed.). O'Reilly Media. 
   - Este libro cubre extensamente el manejo de archivos en Python, incluyendo la lectura y escritura de archivos de texto.

2. Sweigart, A. (2019). Automate the Boring Stuff with Python: Practical Programming for Total Beginners (2nd ed.). No Starch Press.
   - Contiene un capítulo sobre organización de archivos que es muy relevante para este tipo de script.

3. Python Software Foundation. (n.d.). os — Miscellaneous operating system interfaces. Python Documentation. https://docs.python.org/3/library/os.html
   - Esta es la documentación oficial del módulo 'os' de Python, que se utiliza en el script para manejar directorios y rutas de archivos.

4. Python Software Foundation. (n.d.). io — Core tools for working with streams. Python Documentation. https://docs.python.org/3/library/io.html
   - esta documentación proporciona información sobre el manejo de flujos de entrada/salida en Python, que es fundamental para entender cómo Python lee y escribe archivos.

5. McKinney, W. (2017). Python for Data Analysis: Data Wrangling with Pandas, NumPy, and IPython (2nd ed.). O'Reilly Media.
   - Aunque se centra más en el análisis de datos, este libro contiene secciones útiles sobre la manipulación de archivos en Python.
