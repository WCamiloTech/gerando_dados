import json
from countries import get_country_code
import pygal
from pygal_maps_world.maps import World
from pygal.style import RotateStyle


# Estilizando mapas-múndi com o Pygal

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
                # Agrupa os países em três níveis populacionais
                cc_pops_1 = {}
                cc_pops_2 = {}
                cc_pops_3 = {}
                for cc, pop in cc_populations.items():
                    if pop < 1000000:
                        cc_pops_1[cc] = pop
                    elif pop < 1000000000:
                        cc_pops_2[cc] = pop
                    else:
                        cc_pops_3[cc] = pop
                    
                    # Vê quantos países estão em cada nível
                    # print(f'cc_pops_1: {len(cc_pops_1)}')
                    # print(f'cc_pops_2: {len(cc_pops_2)}')
                    # print(f'cc_pops_3: {len(cc_pops_3)}')
                        
                wm_style = RotateStyle('#336699')
                wm = World(style=wm_style)
                wm.title = 'World Population in 2010, by Country'
                wm.add('0-10m', cc_pops_1)
                wm.add('10m-1bn', cc_pops_2)
                wm.add('>1bn', cc_pops_3)
                wm.render_to_file('world_population_3.svg')
