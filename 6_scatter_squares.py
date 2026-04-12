import matplotlib.pyplot as plt

#Colormaps

x_values = list(range(1001))
y_values = [x**2 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolors='none', s=40)

# Define o título do gráfico e nomeia os eixos
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

#Define o intervalo para cada eixo
plt.axis([0, 1100, 0, 1100000])

# Define o tamanho dos rótulos das marcações
plt.tick_params(axis="both", which="major", labelsize=14)

#Desativando notação cientifica no eixo y
plt.ticklabel_format(style="plain", axis="y")

plt.show()
