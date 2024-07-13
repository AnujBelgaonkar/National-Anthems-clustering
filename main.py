import folium
import geopandas as gpd
import pandas as pd
from shapely import wkt
import streamlit as st
from streamlit_folium import st_folium
from utils.plotmap import load_data,create_map
st.set_page_config(layout='wide')


def main():
    left,right = st.columns(2)
    with left:
        clusters = st.slider(label='Cluster Numbers',min_value=5,max_value=20,)
        gdf = load_data(clusters)
        m = create_map(gdf)
        st_folium(m,height=400,width=700)



if __name__ == "__main__": 
    main()