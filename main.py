import folium
from folium.map import Icon

#Creating a basse map
my_map = folium.Map(location = [38.58, -99.09], zoom_start = 5, tiles = "Stamen Terrain")

#Saving the map
my_map.save("My Map.html")