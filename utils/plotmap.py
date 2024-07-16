import folium
import geopandas as gpd
import pandas as pd
from shapely import wkt
import streamlit as st
from streamlit_folium import st_folium
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000']

@st.cache_data
def load_data(clusters):
    df = pd.read_csv("data\geoplots\kmeans{}.csv".format(clusters))
    df['geometry'] = df['geometry'].apply(wkt.loads)
    df['Label'] = df['Label']+1
    gdf = gpd.GeoDataFrame(df, geometry='geometry', crs="EPSG:4326")
    return gdf

def create_map(gdf):
    m = folium.Map(location=[0, 0], zoom_start=2, max_bounds=True,max_zoom=4,min_zoom=2,tiles='Esri WorldImagery')
    label_colors = {label: colors[i] for i, label in enumerate(gdf['Label'].unique())}
    folium.GeoJson(
        gdf,
        name='nationalanthems', 
        style_function=lambda feature: {
            'fillColor': label_colors[feature['properties']['Label']],
            'color': 'black',
            'weight': 1,
            'fillOpacity': 0.5,
        },
        tooltip=folium.GeoJsonTooltip(fields=['Label','name'], aliases=['Cluster:','Country:'])
    ).add_to(m)
    return m
