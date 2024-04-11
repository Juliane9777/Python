import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Datos de ejemplo: años de experiencia y salario
años_experiencia = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]).reshape(-1, 1)
salario = np.array([20000, 25000, 32000, 37000, 42000, 50000, 60000, 65000, 70000, 75000])

# Crear y entrenar el modelo de regresión lineal
modelo = LinearRegression()
modelo.fit(años_experiencia, salario)

# Predecir el salario para años de experiencia futuros
años_futuros = np.array([11, 12, 13, 14, 15]).reshape(-1, 1)
salario_predicho = modelo.predict(años_futuros)

# Graficar los datos y la línea de regresión
plt.scatter(años_experiencia, salario, color='blue', label='Datos')
plt.plot(años_futuros, salario_predicho, color='red', label='Regresión lineal')
plt.xlabel('Años de experiencia')
plt.ylabel('Salario')
plt.title('Regresión lineal: Salario vs. Años de experiencia')
plt.legend()
plt.show()

# Mostrar la pendiente y la intersección
print("Pendiente:", modelo.coef_[0])
print("Intersección:", modelo.intercept_)
