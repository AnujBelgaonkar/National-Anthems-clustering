import os
import streamlit as st
dir = r'E:\Projects\National Anthems\images\mapofwords'

def showcloud(k,cluster):
    folder_dir = os.path.join(dir,f'kmeans{k}')
    image_dir = os.path.join(folder_dir,f'cluster{cluster}.png')
    with st.expander("Word Cloud"):
        st.image(image_dir)