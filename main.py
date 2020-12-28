import folium
import pandas as pd

#Load the data
data = pd.read_csv("Volcanoes.txt")

#Create seperate lists from the data for better understanding
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name = list(data["NAME"])

html = """
Volcano name:<br>
<a href="https://www.google.com/search?q=%%22%s%%22" target="_blank">%s</a><br>
Height: %s m
"""

#Function to define Icon color
def color_generator(elevation):
    if elevation < 1000:
        return "green"
    elif 1000 <= elevation < 3000:
        return "orange"
    else:
        return "red"

#Creating a base map
my_map = folium.Map(location = [38.58, -99.09], zoom_start = 5, tiles = "Stamen Terrain")

#Creating a feature group for better understanding
fg = folium.FeatureGroup(name = "My Map")

#Adding a marker to the fg
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=100)

    fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=folium.Popup(iframe), fill_color = color_generator(el), color = "gray", fill_opacity = 0.7))

fg.add_child(folium.GeoJson(data = open("world.json", "r", encoding = "utf-8-sig").read()))

my_map.add_child(fg)

#Saving the map
my_map.save("My Map.html")