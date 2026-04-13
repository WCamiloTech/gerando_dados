# Plotando os pontos de início e de fim

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Cria um passeio aleatório e plota os pontos
while True:
    #Criar um passeio aleatório e plota os pontos
    rw = RandomWalk()
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none", s=15)
    # Enfatiza o primeiro e o último ponto
    plt.scatter(0, 0, c="green", edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ").upper()
    if keep_running == "N":
        break
