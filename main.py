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
fgv = folium.FeatureGroup(name = "Volcanoes")

#Adding a marker to the fg
for lt, ln, el, name in zip(lat, lon, elev, name):
    iframe = folium.IFrame(html=html % (name, name, el), width=200, height=80)

    fgv.add_child(folium.Marker(location=[lt, ln], popup=folium.Popup(iframe), icon=folium.Icon(color= color_generator(el))))

fgp = folium.FeatureGroup(name = "Population")

fgp.add_child(folium.GeoJson(
    data = open("world.json", "r", encoding = "utf-8-sig").read(),
    style_function = lambda x: {"fillColor": "green" if x["properties"]["POP2005"] < 10000000 
    else "yellow" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))

my_map.add_child(fgv)
my_map.add_child(fgp)

#Layer control panel
my_map.add_child(folium.LayerControl())

#Saving the map
my_map.save("My Map.html")