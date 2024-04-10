#Programa que simula un numero de lanzamientos de una moneda y da el resultado a traves de una gráfica 
#del numero de caras y cruces que han salido
from random import randint
import matplotlib.pyplot as plt
cara=0
cruz=0
numero_lanzamientos = 20000
for i in range(1,numero_lanzamientos + 1):
    valor=randint(0,1)
    if(valor==1):
        moneda="cara"
        cara+=1
    else:
        moneda="cruz"
        cruz+=1
    
    print("El lanzamiento numero: " ,i, "fué" ,moneda )

etiquetas=["cara","cruz"] 
resultados=[cara,cruz]        
plt.bar(etiquetas, resultados)
plt.title("Grafica de resultados")
plt.show()
