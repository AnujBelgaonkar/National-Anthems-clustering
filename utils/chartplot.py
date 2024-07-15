import pandas as pd
import streamlit as st
import plotly.express as px
colors = ['#e6194b', '#3cb44b', '#ffe119', '#4363d8', '#f58231', '#911eb4', '#46f0f0', '#f032e6', '#bcf60c', '#fabebe', '#008080', '#e6beff', '#9a6324', '#fffac8', '#800000', '#aaffc3', '#808000', '#ffd8b1', '#000075', '#808080', '#ffffff', '#000000']


@st.cache_data
def freqworddata(k,cluster):
    data = pd.read_csv(r'E:\Projects\National Anthems\data\wordcounts\word_count_df_kmeans{}.csv'.format(k))
    data['category'] = data['category']+1
    cluster_data = data[data['category'] == cluster]
    cluster_data = cluster_data.sort_values(by = 'count').tail(10)
    return cluster_data

def plotfreqwords(k,cluster):
    cluster_data = freqworddata(k,cluster)
    if not cluster_data.empty:
        fig = px.bar(cluster_data,x = 'count', y = 'word', orientation='h',color='count',height=400)
        return fig

    else:
        st.write("No data available for the specified cluster number.")

@st.cache_data
def pieplotdata(k):
    labels= pd.read_csv(f'E:/Projects/National Anthems/labels/kmeans{k}.csv')
    labels = labels + 1
    data = pd.read_csv(r'E:\Projects\National Anthems\data\national_anthems.csv')
    data = data['Country']
    final = pd.concat([data,labels],axis=1)
    final = final.groupby('Label',as_index=False).count()
    final.rename(columns={"Label" : "Cluster", "Country":"Count"},inplace=True)
    return final

def pieplot(k):
    final = pieplotdata(k)
    label_colors = {label: colors[i] for i, label in enumerate(final['Cluster'].unique())}
    fig = px.pie(final,values='Count',names='Cluster',
color_discrete_map=label_colors,title="                                                                         Cluster Distribution")
    st.plotly_chart(fig)





