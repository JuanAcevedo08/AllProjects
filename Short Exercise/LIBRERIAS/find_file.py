import os

cwd = os.getcwd()

archivo = [f for f in os.listdir(cwd) if f.endswith('.json')]
print(archivo)