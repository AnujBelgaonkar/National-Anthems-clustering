import streamlit as st
from annotated_text import annotated_text
import pandas as pd
from nltk import word_tokenize
from Preprocessing import pos_tag_tokens
def annotateanthme(country):
    df = pd.read_csv(r"E:\Projects\National Anthems\data\national_anthems.csv")
    st.write(df)
    anthem = df[df['Country'] == country]['Anthem']
    st.write(anthem)
    listoftokens = word_tokenize(str(anthem.iloc[0]))
    taggedtokens = pos_tag_tokens(listoftokens)
    st.write(taggedtokens)
    

annotateanthme('India')