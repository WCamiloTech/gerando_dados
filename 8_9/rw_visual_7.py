# Alterando o tamanho para preencher a tela

import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Cria um passeio aleatório e plota os pontos
while True:
    #Criar um passeio aleatório e plota os pontos
    rw = RandomWalk(50000)
    rw.fill_walk()
    
    # Define o tamanho da janela de plotagem 
    plt.figure(figsize=(10, 6))
    
    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors="none", s=1)
    
    # Enfatiza o primeiro e o último ponto
    plt.scatter(0, 0, c="green", edgecolors="none", s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)
    
    #Remove os eixos
    plt.axis('off')
    
    plt.show()
    
    keep_running = input("Make another walk? (y/n): ").upper()
    if keep_running == "N":
        break
