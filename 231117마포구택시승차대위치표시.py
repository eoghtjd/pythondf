import pandas as pd
import folium 

data = pd.read_csv("C:\\Users\\H\\Desktop\\github\\python\\택시승차대 현황.csv", encoding='cp949')

#위도,경도

위도 = data['위도']  
경도 = data['경도']  

m = folium.Map(location=[위도[0], 경도[0]], zoom_start=15)  # 위도와 경도 중 첫 번째 데이터를 기준으로 지도 생성

for i in range(len(data)):
    folium.Marker([위도[i], 경도[i]], popup='택시승강장', icon=folium.Icon(color='red', icon='fa-solid fa-taxi', prefix='fa-solid')).add_to(m)
