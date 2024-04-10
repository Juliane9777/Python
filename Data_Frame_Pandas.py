import pandas as pd

# Crear un DataFrame de ejemplo
data = {'Nombre': ['Juan', 'María', 'Pedro', 'Luis', 'Ana'],
        'Edad': [25, 30, 35, 40, 45],
        'Puntuación': [70, 85, 90, 88, 82]}

df = pd.DataFrame(data)

# Mostrar el DataFrame
print("Datos originales:")
print(df)

# Calcular estadísticas básicas
print("\nEstadísticas básicas:")
print(df.describe())

# Calcular la media de la puntuación
media_puntuacion = df['Puntuación'].mean()
print("\nMedia de la puntuación:", media_puntuacion)
