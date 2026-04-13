import matplotlib.pyplot as plt
from random_walk import RandomWalk

# Cria um passeio aleatório e plota os pontos
while True:
    #Criar um passeio aleatório e plota os pontos
    rw = RandomWalk()
    rw.fill_walk()
    plt.scatter(rw.x_values, rw.y_values, s=15)
    plt.show()
    keep_running = input("Make another walk? (y/n): ").upper()
    if keep_running == 'N':
        break
