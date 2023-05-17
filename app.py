#Import Python Libs
import streamlit as st
import requests
import geopandas as gpd
import folium
import json
# Main Streamlit app
def main():
    st.title("Freedmen Colonies")
# Input GitHub GeoJSON URL
geojson_url = st.text_input("https://raw.githubusercontent.com/rmkenv/CLP/main/clp_fc.geojson")
 # Fetch GeoJSON data
    if geojson_url:
        response = requests.get(geojson_url)
        if response.status_code == 200:
            geojson_data = response.json()

            # Create GeoDataFrame
            features = geojson_data['features']
            gdf = gpd.GeoDataFrame.from_features(features)

            # Display fetched data
            st.subheader("Data from GeoJSON")
            st.dataframe(gdf)

            # Create map
            st.subheader("Map")
            map_center = [gdf['geometry'].centroid.y.mean(), gdf['geometry'].centroid.x.mean()]
            m = folium.Map(location=map_center, zoom_start=10)

            # Add GeoJSON layer to the map
            folium.GeoJson(geojson_data, name='geojson').add_to(m)

            # Display the map
            st.markdown(m._repr_html_(), unsafe_allow_html=True)
        else:
            st.error("Error retrieving GeoJSON data.")

if __name__ == "__main__":
  main()
