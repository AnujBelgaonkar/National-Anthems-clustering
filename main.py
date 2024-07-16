import folium
import geopandas as gpd
import pandas as pd
from shapely import wkt
import streamlit as st
from streamlit_folium import st_folium
from utils.plotmap import load_data, create_map
from utils.chartplot import plotfreqwords, pieplot

st.set_page_config(
    page_title='National Anthems Analysis',
    layout='wide',
    page_icon=':earth_asia:'
)

def main():
    # Centering the title using HTML with additional styling
    st.markdown(
        """
        <style>
        .centered-title {
            text-align: center;
            font-size: 3em;
        }
        .container {
            padding: 10px;
        }
        </style>
        <div class="centered-title">National Anthem Clusters Analysis</div>
        """,
        unsafe_allow_html=True
    )

    left, right = st.columns(2, gap='small')
    with left:
        k = st.slider(label='Select number of clusters', min_value=5, max_value=20)
        gdf = load_data(k)
        if not gdf.empty:
            with st.container(height=360):  # Wrap the map rendering inside a container
                m = create_map(gdf)
                st_folium(m, height=360, width=800)  # Set height and width explicitly
    with right:
        with st.container(border=False):
            pieplot(k)
    falseleft,middle,falseright = st.columns([1,3,1],gap = 'medium')
    with middle:
        with st.container():
            selected_cluster = st.slider(label="Select Cluster", min_value=1, max_value=k)
            freqgraph = plotfreqwords(k, cluster=selected_cluster)
            temp = st.plotly_chart(freqgraph, use_container_width=True)
if __name__ == "__main__": 
    main()