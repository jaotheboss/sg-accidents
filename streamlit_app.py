import streamlit as st
import pandas as pd
import folium
from folium import plugins
from streamlit_folium import st_folium

@st.cache_resource
def load_data():
   df = pd.read_csv(st.secrets["data_url"]) 
   return df

@st.cache_data
def export_data(df):
   return df.to_csv(index=False).encode('utf-8')

df = load_data()
csv = export_data(df)

st.subheader("Map")
map = folium.Map([1.3500,103.8850], zoom_start=11.1)
location_data = df[['Latitude', 'Longitude']].to_numpy()
# plot heatmap
map.add_children(plugins.HeatMap(location_data, radius=10))

st_map = st_folium(map, width=900, height=450)

st.subheader("Latest occurences:")
st.dataframe(df.head(10))
st.download_button(
   "Download",
   csv,
   "sg_accidents_data.csv",
   "text/csv",
   key='download-csv'
)