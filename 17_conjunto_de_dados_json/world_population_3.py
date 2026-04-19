import json
from countries import get_country_code

# Obtendo os códigos de duas letras dos países

# Carrega os dados em uma lista
filename = 'population_data.json'

with open(filename) as f:
    pop_data = json.load(f)
    
    # Exibe a população de cada país em 2010
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            
            if code:
                print(f'{code}: {population}')
                # print(f'{country_name}: {population}')
            else:
                print(f'ERRO - {country_name}')