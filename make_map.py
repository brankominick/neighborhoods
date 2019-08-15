import pandas as pd
import folium
import json 

xls = pd.ExcelFile('neighborhoodsummaryclean_1950-2010.xlsx')
neighborhoods = xls.sheet_names

yr1950 = []
yr1960 = []
yr1970 = []
yr1980 = []
yr1990 = []
yr2000 = []
yr2010 = []


for i in neighborhoods:
    df = xls.parse(i)
    yr1950.append(df[1950].iloc[0])
    yr1960.append(df[1960].iloc[0])
    yr1970.append(df[1970].iloc[0])
    yr1980.append(df[1980].iloc[0])
    yr1990.append(df[1990].iloc[0])
    yr2000.append(df[2000].iloc[0])
    yr2010.append(df[2010].iloc[0])
    
data = {'Neighborhoods':neighborhoods, 'yr1950':yr1950, 'yr1960':yr1960
        ,'yr1970':yr1970, 'yr1980':yr1980, 'yr1990':yr1990, 'yr2000':yr2000
        ,'yr2010':yr2010}

df = pd.DataFrame(data=data)


    
with open('Boston_Neighborhoods.geojson', 'r') as file:
    listed_neighborhoods = json.load(file)

"""boundaries = []
for i in range(len(listed_neighborhoods['features'])):
    if listed_neighborhoods['features'][i]['properties']['Name'] in neighborhoods:
        boundaries.append(listed_neighborhoods['features'][i])"""


years = ['yr1950','yr1960','yr1970','yr1980','yr1990','yr2000','yr2010']
for i in range(len(years)):
    map = folium.Map(location = [42.3601, -71.0589]
                    ,zoom_start = 11
                )
    folium.Choropleth(
            geo_data = listed_neighborhoods
            ,fill_opacity = 0.8
            ,line_opacity = 0.2
            ,data = df
            ,columns = ['Neighborhoods', years[i]]
            ,key_on = 'properties.Name'
            ,fill_color = 'YlGn'
            ,legend_name = 'Population by Neighborhood' + years[i]
        ).add_to(map)
    folium.LayerControl().add_to(map)
    map.save(outfile = 'index'+years[i]+'.html')
        

print('done')