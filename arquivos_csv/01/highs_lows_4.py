import csv

# Extraindo e lendo os dados

# Obtém as temperaturas máximas do arquivo
# Coverendo strings em números
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
    
            
        
    