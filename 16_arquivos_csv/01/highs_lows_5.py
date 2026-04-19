import csv
from matplotlib import pyplot as plt
# Extraindo e lendo os dados

# Plotando dados em um gráfico de temperatura
filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    highs = []
    
    # for index, column_header in enumerate(header_row):
    #     print(index, column_header)
    
    for row in reader:
        high = int(row[1])
        highs.append(high)

    print(highs)
    
    # Faz a plotagem dos dados
    fig = plt.figure(dpi=128, figsize=(10, 6))
    plt.plot(highs, c='red')
    
    # Formata o gráfico
    plt.title('Daily high temperatures, July 2014', fontsize=24)
    plt.xlabel('', fontsize=16)
    plt.ylabel('Temperature (F)', fontsize=16)
    plt.tick_params(axis='y', which='major', labelsize=16)
    
    # Cria uma lista de 1 até o total de dias (ex: 1 a 31)
    dias = list(range(1, len(highs) + 1))
    
    # Define que os rótulos do eixo X serão esses dias, de 1 em 1
    plt.xticks(dias)
    
    # Ajusta o limite para tocar as bordas
    plt.xlim(0, len(highs) - 1)
    
    plt.show()

    
            
        
    