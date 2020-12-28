import folium
import pandas as pd

#Load the data
data = pd.read_csv("Volcanoes.txt")

#Create seperate lists from the data for better understanding
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

#Creating a basse map
my_map = folium.Map(location = [38.58, -99.09], zoom_start = 5, tiles = "Stamen Terrain")

#Adding a marker
for lt, ln, el in zip(lat, lon, elev):
    folium.Marker(location = [lt, ln], popup = str(el) + " m", icon = folium.Icon(color = "blue")).add_to(my_map)

#Saving the map
my_map.save("My Map.html")