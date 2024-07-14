import folium
import geopandas as gpd
import pandas as pd
from shapely import wkt
import streamlit as st
from streamlit_folium import st_folium
from utils.plotmap import load_data,create_map
from utils.chartplot import plotfreqwords,pieplot
from utils.wordcloud import showcloud
st.set_page_config(layout='wide')


def main():
    left,right = st.columns(2,gap='large')
    with left:
        k = st.slider(label='Cluster Numbers',min_value=5,max_value=20,)
        gdf = load_data(k)
        m = create_map(gdf)
        st_folium(m,height=350,width=700)
        pieplot(k)

    with right:
        selected_cluster = st.slider(label="Cluster Number",min_value=0,max_value=k-1)
        plotfreqwords(k,cluster= selected_cluster)
        showcloud(k,cluster=selected_cluster)
        

if __name__ == "__main__": 
    main()