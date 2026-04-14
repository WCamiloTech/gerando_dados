from die import Die

# Analisando os resultados
# Cria um D6
die = Die()

# Faz alguns lançamentos e armazena os resultados em uma lista
results = []

for roll_num in range(1000):
    result = die.roll()
    results.append(result)

print(results)

# Analisa os resultados
frequencies = []

for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
    
print(frequencies)
