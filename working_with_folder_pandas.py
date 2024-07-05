#=========================Librerías================================================
# Libraries required for data analysis and preprocessing
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
 
# Libraries required for data visualization
import matplotlib.pyplot as plt
import seaborn as sns
 
# Libraries required for linear regression model application
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error
 
# Libraries required for residualization
import scipy.stats
 
#Setting the route 
import os 
from pathlib import Path
import tensorflow
 
#Zipping
import zipfile
 
 
#=====================Rutas=====================================
def new_route(route_file):
    base_route = Path.home()
    complete_route = os.path.join(base_route, route_file)
    return complete_route
all_routes = new_route("Desktop\datos.zip")
print(all_routes)
 
 
def new_route_destino(route_file):
    base_route = Path.home()
    complete_route = os.path.join(base_route, route_file)
    return complete_route
ruta_destino = new_route("Desktop")
print(ruta_destino)
 
 
#======================Extrayendo datos =====================
 
# Define la ruta del archivo zip que has subido
zip_path = all_routes  # Cambia esta ruta según sea necesario
 
# Define el directorio de destino donde se extraerán los archivos
extract_to = ruta_destino  # Cambia esta ruta según sea necesario
 
# Verifica si la ruta del archivo zip existe
if not os.path.isfile(zip_path):
    raise FileNotFoundError(f"El archivo {zip_path} no existe.")
 
# Crea el directorio de destino si no existe
if not os.path.isdir(extract_to):
    os.makedirs(extract_to)
 
# Descomprime el archivo zip
try:
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(extract_to)
    print(f"Archivos extraídos en {extract_to}")
except zipfile.BadZipFile:
    print(f"Error: El archivo {zip_path} no es un archivo zip válido.")
except Exception as e:
    print(f"Ocurrió un error al descomprimir {zip_path}: {e}")
 
#============================Ruta final=================================
 
def new_route_destino(route_file):
    base_route = Path.home()
    complete_route = os.path.join(base_route, route_file)
    return complete_route
ruta_final = new_route("Desktop\datos")
 
#==============================Uniendo todos los csv ==============================
 
def leer_y_concatenar_csv(carpeta):
    archivos_csv = [f for f in os.listdir(carpeta) if f.endswith('.csv')]
    df_list = []
    for archivo in archivos_csv:
        archivo_path = os.path.join(carpeta, archivo)
        df = pd.read_csv(archivo_path, sep='|')  # Ajusta el delimitador según sea necesario
        df_list.append(df)
    # Concatenar todos los DataFrames en uno solo
    df_concatenado = pd.concat(df_list, ignore_index=True)
    return df_concatenado
 
# Ruta de la carpeta descomprimida
ruta_carpeta = 'directorio_de_destino'  # Cambia esta ruta según sea necesario
 
# Leer y concatenar los archivos CSV en la carpeta
df_concatenado = leer_y_concatenar_csv(ruta_final)
 
# Mostrar las primeras filas del DataFrame concatenado
print(df_concatenado.head())
 
#A partir de aquí ya se pueden usar las funciones de pandas.