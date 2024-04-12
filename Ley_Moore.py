import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

# Leemos el archivo CSV. Como el delimitador es ';', lo especificamos en la función read_csv.
df = pd.read_csv('raw_data.csv', delimiter=';')

# Aplicamos una transformación logarítmica a los datos de los transistores.
df['log_Transistores'] = np.log(df['Transistors'])

# Creamos una instancia del modelo de regresión lineal
modelo = LinearRegression()

# Ajustamos el modelo a nuestros datos. Usamos el año como variable independiente y el logaritmo del número de transistores como variable dependiente.
modelo.fit(df[['Year']], df['log_Transistores'])

# Ahora podemos usar nuestro modelo para hacer predicciones
df['prediccion'] = modelo.predict(df[['Year']])

# Revertimos la transformación logarítmica para visualizar los datos en su escala original
df['Transistores_predichos'] = np.exp(df['prediccion'])

# Y finalmente, podemos visualizar los resultados
plt.scatter(df['Year'], df['Transistors'], color='blue')
plt.plot(df['Year'], df['Transistores_predichos'], color='red')

# Establecemos la escala del eje y en logarítmica y especificamos los ticks
plt.yscale('log')
plt.yticks([2300,10**4, 10**5, 10**6, 10**7, 10**8, 10**9, 10**10], ['2300','10,000', '100,000', '1,000,000', '10,000,000', '100,000,000', '1,000,000,000', '10,000,000,000'])
plt.xticks([1970,1975,1980,1985,1990,1995,2000,2005,2010,2014],['1970','1975','1980','1985','1990','1995','2000','2005','2010','2014'])

plt.xlabel('Año')
plt.ylabel('Número de Transistores')
plt.title('Regresión lineal aplicada a la Ley de Moore')
plt.show()
