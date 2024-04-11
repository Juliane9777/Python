#Script que mediante regresion lineal calcula la temperatura media de un mes de la ciudad de nueva York
#Teniendo en cuenta las temperaturas medias de los años del 1985 al 2023 usadas en data_New_York.csv
#-----------------------------------------------------------------------------------------------------
#Cargar bibliotecas necesarias
import pandas as pd
from scipy import stats
#Cargamos los datos
print("Cargando datos...")
try:
    nueva_york=pd.read_csv('data_New_York.csv')
    print("Datos cargados correctamente.")

except Exception as e:
    print("Error al cargar los datos:", e)

#Cambiamos el nombre de las columnas
nueva_york.columns = ['Fecha', 'Temperatura', 'Anomalía']
#Eliminamos el mes 07 dividiendo cada fecha entre 100
nueva_york.Fecha = nueva_york.Fecha.floordiv(100)
#Conveertir fahrenheit a grados centigrados
for i in nueva_york.index:
    nueva_york.Temperatura[i] = 5/9 * (nueva_york.Temperatura[i]-32)
#Imprimir dataset completo con los cambios
print("Dataset compleeto ya con cambios: \n" ,nueva_york)
#Imprimir valores estadisticos
print("Valores estadisticos del Dataset:" ,nueva_york.Temperatura.describe())
#Ahora predecimos la temp y = mx + b
regresion_lineal = stats.linregress(x=nueva_york.Fecha, y=nueva_york.Temperatura)
m = regresion_lineal.slope
x = 2024
b = regresion_lineal.intercept
estimacion = m * x + b
print("La temperatura media estimada para julio del 2024 es:" ,estimacion,"\n")
