import os
#Mostrar la ruta del directorio actual
cwd = os.getcwd()

#Busqueda de archivo en un directorio
ls = [f for f in os.listdir('.')if f.endswith('.py')] #Me muestra todos los archivos py del directorio actual
#Rename Files
#os.rename('buscar archivo.py', 'find_file.py')
os.rename('clase 27.py', 'LIBRERIA_CON_OS.py')

files = [f for f in os.listdir(cwd) if f.endswith('.py')]
print(files)
