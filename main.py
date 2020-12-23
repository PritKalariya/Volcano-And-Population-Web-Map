import folium

#Creating a basse map
my_map = folium.Map(location = [38.58, -99.09], zoom_start = 5, tiles = "Stamen Terrain")

#Adding a marker
for coordinates in [[38.2, -99.1], [40.2, -96.1]]:
    folium.Marker(location = coordinates, popup = "Hii!! I'm a marker", icon = folium.Icon(color = "blue")).add_to(my_map)

#Saving the map
my_map.save("My Map.html")