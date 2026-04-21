import pygal
import requests
from pygal.style import LightColorizedStyle as LCS
from pygal.style import RotateStyle as RS
from pygal.style import LightenStyle as LS

# Aperfeiçoando os gráficos do Pygal

# Faz uma chamada de API e armazena a resposta
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print(f'Status code: {r.status_code}')

# Armazena a resposta da API em uma variável
response_dict = r.json()

# Processa o resultado
print(response_dict.keys())

# Armazena a respota da API em um variável
print(f"Total repositórios: {response_dict['total_count']}")

# Explora informações sobre os repositórios
repo_dicts = response_dict['items']
names = []
stars = []
print(f'Repositories returned: {len(repo_dicts)}')
print("\nSelected information about each repository:")

for repo_dict in repo_dicts:
    names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    
    # Cria a visualização
    my_style = LS('#333366', base_style=LCS)
    my_config = pygal.Config()
    my_config.x_label_rotation = 45
    my_config.show_legend = False
    my_config.title_font_size = 24
    my_config.label_font_size = 14
    my_config.major_label_font_size = 18
    my_config.truncate_label = 15
    my_config.show_y_guides = False
    my_config.width = 1000
    chart = pygal.Bar(my_config, style=my_style)
    chart.title = 'Most-Starred Python Projects on GitHub'
    chart.x_labels = names
    chart.add('', stars)
    chart.render_to_file('python_repos_2.svg')




