import folium

map = folium.Map(location=[50.2871, 21.4238])

i = 1;
for coordinates in [[51.2777, 21.4320],[50.2777, 23.4000],[37.2777, 21.4000],[55.2777, 19.4000]]:
    map.add_child(folium.Marker(location=coordinates, popup="Tn", icon=folium.Icon(color='blue')))

map.save("map.html")

help(folium.Map)