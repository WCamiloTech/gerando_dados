from pygal_maps_world.maps import World

# Plotando dados numéricos em um mapa-múndi

vw = World()
vw.title = "Populations of Countries in North America"
vw.add("North America", {"ca": 34126000, "us": 309349000, "mx": 113423000})
vw.render_to_file('na_populations.svg')
