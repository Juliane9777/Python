from random import randint
import matplotlib.pyplot as plt

simulaciones = 0  # Contador de simulaciones
total_ganado = 0  # Variable para almacenar el total ganado en todas las simulaciones

while True:
    cantidad_apostada = 0.125
    cantidad_ganada = 0
    num_apuestas = 0
    limite_apostado = 63  # Límite máximo de dinero a apostar
    color = "rojo"
    ganancias = []  # Lista para almacenar las ganancias en cada apuesta
    a = 0
    b = 0
    consecutivo_no_rojo = 0  # Contador para tiradas consecutivas en las que no sale rojo y pierdes

    while consecutivo_no_rojo <= 10 and num_apuestas <= 1000:
        num_apuestas += 1
        valor = randint(1, 38)  # Cambiar el rango a 1-38

        if valor <= 18:  # Si el número está en el rango de casillas rojas, ganas
            cantidad_ganada += cantidad_apostada
            cantidad_apostada = 0.125
            decision = "has ganado"
            color = "\033[31mrojo\033[0m"  # Rojo
            b += 1
            consecutivo_no_rojo = 0  # Reiniciar contador si se gana en esta tirada
        else:  # Pierdes
            cantidad_ganada -= cantidad_apostada
            cantidad_apostada *= 2
            decision = "has perdido"
            color = "\033[34mazul oscuro\033[0m"  # Azul oscuro
            a += 1
            consecutivo_no_rojo += 1 

        print("Apuesta", num_apuestas, "ha salido", color, "y tienes un saldo total de:", cantidad_ganada, "€")

        ganancias.append(cantidad_ganada)  # Agregar la cantidad ganada a la lista

    simulaciones += 1

    print("\nSimulación", simulaciones)
    print("La cantidad ganada en esta simulación es:", cantidad_ganada)
    print("Apuestas ganadas:", b)
    print("Apuestas perdidas:", a)
    print("Se ha alcanzado el límite máximo de dinero apostado.")

    # Sumar la cantidad ganada en esta simulación al total ganado
    total_ganado += cantidad_ganada

    # Si la cantidad ganada es negativa, salir del bucle
    if cantidad_ganada < 0:
        break

# Graficar las ganancias
plt.plot(range(1, num_apuestas + 1), ganancias)
plt.xlabel('Número de Apuestas')
plt.ylabel('Ganancias')
plt.title('Evolución de las Ganancias en la Martingala')
plt.grid(True)
plt.show()

print("\nTotal de simulaciones:", simulaciones)
print("Total ganado en todas las simulaciones:", total_ganado)
