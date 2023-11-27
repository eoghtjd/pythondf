import folium
m=folium.Map(location=[37.547631,126.942463],zoom_start=15)

folium.Marker([37.547631,126.942463]).add_to(m)
folium.Marker([37.5476312,126.9510],popup='subway').add_to(m)
#print(m)
