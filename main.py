import folium
import geopandas as gpd
import pandas as pd
from shapely import wkt
import streamlit as st
from streamlit_folium import st_folium
from utils.plotmap import load_data,create_map
from utils.chartplot import plotfreqwords,pieplot
st.set_page_config(layout='wide')

def main():
    left,right = st.columns(2,gap='medium')
    with left:
        k = st.slider(label='Cluster Numbers',min_value=5,max_value=20,)
        gdf = load_data(k)
        if not gdf.empty:
            with st.container():
                m = create_map(gdf)
                st_folium(m,height=350,width=700) 
                
            
     

    with right:
        with st.container(border=False):
            pieplot(k)
        with st.container():
            selected_cluster = st.slider(label="Cluster Number",min_value=1,max_value=k)
            freqgraph = plotfreqwords(k,cluster= selected_cluster)
            st.plotly_chart(freqgraph,use_container_width=True)

if __name__ == "__main__": 
    main()