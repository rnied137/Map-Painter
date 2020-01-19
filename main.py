import folium
import pandas
import csv
from GPS import GPS

csv_file =  open("worldcities.csv", 'r', encoding="utf8")
colnames = ["city","city_ascii","lat","lng"]
coord_list =[[]]
#lat
#lon

i = 1;



data = pandas.read_csv("worlds2.csv", sep=';')
lat = list(data["lat"])
lon = list(data["lng"])
        #coord_list.append(lat,lon)

#print(coord_list)
#for x in range(len(coord_list)):
 #   print (coord_list[x])
  #  print(coord_list[x])




map = folium.Map(location=[50.2871, 21.4238])

#i = 1;
for lt, ln in zip(lat,lon):
    map.add_child(folium.Marker(location=[lt, ln], popup="Tn", icon=folium.Icon(color='blue')))

map.save("map.html")

