import pandas
import folium
import json
import urllib.request

covid_df = pandas.read_json("https://pomber.github.io/covid19/timeseries.json")

#Get the latest entry for each country
covid_lastentry_df = covid_df.iloc[[-1]]

#Get Lat/Lon for each country
with open('world.json','rb') as f:
   data = json.load(f)

dataframe = pandas.DataFrame(columns=['NAME', 'LAT', 'LON'])
for i in data["features"]:
    dataframe = dataframe.append({'NAME': i.get('properties').get('NAME'), 'LAT': i.get('properties').get('LAT'), 'LON': i.get('properties').get('LON')}, ignore_index=True)

lat = list(dataframe["LAT"])
lon = list(dataframe["LON"])
name = list(dataframe["NAME"])


#fix some of the name mismatches between datasets
name = [n.replace('United States', 'US') for n in name]
name = [n.replace('Viet Nam', 'Vietnam') for n in name]
name = [n.replace('Iran (Islamic Republic of)', 'Iran') for n in name]

html = """
    <h4>Covid-19 information:</h4> 
    Country: %s <br>
    Confirmed: %s <br>
    Deaths: %s <br>
    Recovered: %s <br>
    Last Updated: %s <br>
    """


map = folium.Map(location=[0, 0], zoom_start=2, tiles="Stamen Terrain")

#Coronavirus infections
fgc = folium.FeatureGroup(name="Covid-19")
for lt, ln, name in zip(lat, lon, name):
    if name in covid_lastentry_df:
        covid_data =  covid_lastentry_df[name]
        iframe = folium.IFrame(html=html % (name, covid_data.item()["confirmed"], covid_data.item()["deaths"], covid_data.item()["recovered"], covid_data.item()["date"]), width=200, height=150)
        fgc.add_child(folium.CircleMarker(location=[lt,ln], popup=folium.Popup(iframe), 
        radius=5, fill_color="Green", fill_opacity = 0.7 ))
    else:
        print(name)



#World Population
fgp = folium.FeatureGroup(name="Population")
fgp.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(),
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))

map.add_child(fgc)
#map.add_child(fgp)
map.add_child(folium.LayerControl())

map.save("map.html")