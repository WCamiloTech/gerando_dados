import json
from countries import get_country_code
import pygal
from pygal_maps_world.maps import World


# Criando um mapa completo de populações

# Carrega os dados em uma lista
filename = 'population_data.json'

with open(filename) as f:
    pop_data = json.load(f)
    
    # Constrói um dicionário com dados das populações
    cc_populations = {}
    
    # Exibe a população de cada país em 2010
    for pop_dict in pop_data:
        if pop_dict['Year'] == '2010':
            country_name = pop_dict['Country Name']
            population = int(float(pop_dict['Value']))
            code = get_country_code(country_name)
            
            if code:
                cc_populations[code] = population
                vw = World()
                vw.title = 'World Population in 2010, by Country'
                vw.add('2010', cc_populations)
                vw.render_to_file('world_population.svg')
