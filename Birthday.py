import random
import matplotlib.pyplot as plt

# Definición de la función que realiza la simulación del problema del cumpleaños
def birthday_paradox_simulation(num_simulations, num_people):
    shared_birthdays_count = 0

    # Realiza 'num_simulations' simulaciones del problema del cumpleaños
    for _ in range(num_simulations):
        # Genera una lista de 'num_people' números aleatorios que representan los días de cumpleaños
        birthdays = [random.randint(1, 365) for _ in range(num_people)]
        
        # Verifica si hay al menos dos personas con cumpleaños compartido
        if len(birthdays) != len(set(birthdays)):
            shared_birthdays_count += 1

    # Calcula la probabilidad de que al menos dos personas compartan cumpleaños
    probability = shared_birthdays_count / num_simulations
    return probability

# Función principal del programa
def main():
    num_simulations = 10000  # Número de simulaciones a realizar
    max_num_people = 50  # Número máximo de personas en el grupo
    probabilities = []  # Lista para almacenar las probabilidades calculadas

    # Realiza la simulación para diferentes tamaños de grupo (número de personas)
    for num_people in range(2, max_num_people + 1):
        probability = birthday_paradox_simulation(num_simulations, num_people)
        probabilities.append(probability)

    # Gráfico de barras que muestra la probabilidad en función del número de personas en el grupo
    plt.bar(range(2, max_num_people + 1), probabilities)
    plt.xlabel('Número de Personas')
    plt.ylabel('Probabilidad')
    plt.title('Probabilidad de que al menos dos personas compartan cumpleaños')
    plt.show()

# Se ejecuta la función principal si el script es ejecutado directamente
if __name__ == "__main__":
    main()
