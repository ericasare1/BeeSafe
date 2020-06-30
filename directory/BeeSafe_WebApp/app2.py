#core pkgs
import streamlit as st
import os
import joblib
from PIL import Image
from sklearn import preprocessing


#EDA pkgs
import pandas as pd
import numpy as np


#Data vis pkgs
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')
import plotly.express as px
import altair as alt
from vega_datasets import data
#other pkgs if needed

#put an image on the page of the app

st.title("BeeSafe WebApp")

picture = Image.open("images/bee.jpg")
st.image(picture, caption = "Bees Love Flower Plants (Source: Swallow Tail Garden)")

#dictionary to get all the variables and encoding to be used in selectbox
#get the keys
def get_values(val, my_dict):
    for key , value in my_dict.items():
        if val == key:
            return value

#find the key from dictionary
def get_key(val, my_dict):
    for key, value in my_dict.items():
        if val == value:
            return key
#dictionaries
county_label = {'Monroe': 0, 'Henry': 1, 'Christian': 2,'Teton': 3, 'McPherson': 4, 'Centre': 5,'Arkansas': 6,'Windham': 7, 'Dane': 8,
                'Belmont': 9, 'Garfield': 10,'Clallam': 11, 'Cherokee': 12, 'Lewis': 13,'Yakima': 14, 'Scotland': 15, 'Cascade': 16, 'Salt Lake': 17,
                'Park': 18, 'Saint Charles': 19, 'Emmons': 20, 'Sierra': 21, 'Yukon-Koyukuk': 22, 'Otero': 23, 'Platte': 24, 'Osage': 25, 'Douglas': 26,
                'Jefferson': 27, 'Lake': 28, 'Johnson': 29,'Whitman': 30, 'Lancaster': 31,'Cocke': 32, 'Socorro': 33,'Box Elder': 34, 'Pope': 35,
                'Ravalli': 36, 'Idaho': 37, 'Chaffee': 38, 'Ogle': 39,'Washakie': 40, 'Weston': 41, 'Lincoln': 42, 'Wasatch': 43,
                 'McDowell': 44,'Goodhue': 45, 'Foster': 46, 'Washington': 47, 'Larimer': 48, 'Franklin': 49, 'Trinity': 50,
                 'Harrison': 51, 'Mahaska': 52, 'Mason': 53, 'Deschutes': 54, 'Bastrop': 55, 'Kenai Peninsula': 56, 'Dutchess': 57, 'Chesterfield': 58,
                 'Champaign': 59,'Clayton': 60,'Peoria': 61, 'Burke': 62, 'Howard': 63, 'Orange': 64,'Marin': 65,
                'Stokes': 66, 'San Juan': 67, 'Valdez-Cordova': 68, 'Sheridan': 69, 'Houston': 70, 'Anchorage': 71, 'Cache': 72,
                'Turner': 73, 'Benton': 74, 'Skagit': 75, 'Linn': 76, 'San Francisco': 77, 'Chelan': 78, 'Union': 79}

Achillea_label = {'Achillea sp.': 1, 'Not Achillea sp.': 0}
Asteraceae_label = {'Asteraceae sp.': 1, 'Not Asteraceae sp.': 0}
Brassica_label = {'Brassica sp.': 1, 'Not Brassica sp': 0}
Cirsium_label = {'Cirsium sp.': 1, 'Not Cirsium sp.': 0}
Delphinium_label = {'Delphinium sp.': 1, 'Not Delphinium sp.': 0}
Epilobium_label = {'Epilobium latifolium': 1, 'Not Epilobium latifolium': 0}
Erigeron_label = {'Erigeron sp.': 1, 'Not Erigeron sp.': 0}
Lotus_label = {'Lotus corniculatus': 1, 'Not Lotus corniculatus': 0}
Phacelia_label = {'Phacelia sp.': 1, 'Not Phacelia sp.': 0}
Rubus_label = {'Rubus allegheniensis': 1, 'Not Rubus allegheniensis': 0}
Scrophularia_label = {'Scrophularia sp.': 1, 'Not Scrophularia sp.': 0}
Lathyrus_label =  {'Lathyrus sp.': 1, 'Not Lathyrus sp.': 0}
#function to load dataset
@st.cache
def load_data():
    data = pd.read_csv("data/streamlit_data.csv")
    return data

def load_data_map():
    data = pd.read_csv("data/plotly_sm.csv")
    return data

#load data and catche it using streamlit cache
bee_data = load_data()
plotly_map = load_data_map()

#read mapbox key
with open('mapbox_tkn.txt', 'r') as f:
    mapbox_key = f.read().strip()

 
#def load_prediction_model(model):
    #loaded_model = joblib.load(open(os.path.join(model_file), "rb"))
    #return loaded_model


def main():
    """Bee WebApp"""

    #Menus or activities and under each menu u populate it with whatever you want to show with the st.write
    menu = ["Exploring Bumble Bee Data", "Predicting Bumble Bee Species Count"]
    choices = st.sidebar.selectbox("select Activities", menu)

    
    if choices == "Exploring Bumble Bee Data":

        st.subheader("Spatial View of Bumble Bee Survey Sites")
       #A spatial map to show the sites where bumble bees were sampled
        fig_map = px.scatter_mapbox(
        plotly_map, lat="lat", lon="lon", size="bee sp. count", hover_name='county', hover_data=['county'], zoom=12)
        # Now using Mapbox
        fig_map.update_layout(mapbox_style="light", autosize=False, width=1120, height=500, mapbox_accesstoken=mapbox_key,
                                margin=dict(l=10, r=10, b=10, t=10, pad=4 ))
        st.plotly_chart(fig_map)

    # Bar chart to show the Top 10 bumble bee count associated with plants using plotly
        st.subheader("Find Out Which Flower Plants Bumble Bees Love")

        state_filter = st.text_input(label = 'Please, input in State name (first letter of state is capitalised)', key = 'state')
        county_filter = st.text_input(label = 'Please, input in County name (first letter of state is capitalised)', key = 'county')
        st.subheader(" Top 10 Bumble Bee Counts Associated with Flower Plants ")
        k =  bee_data[(bee_data['state'] == state_filter)][bee_data['county']== county_filter].nlargest(10, ['bee count'])     
        fig = px.bar(k, x='plant', y='bee count', color='bee count',
                 labels={'plant': 'Plant Type', 'bee count': 'Bumble Bee Count'})
        st.plotly_chart(fig)

        # st.write(data['class'].value_count().plot(kind = "bar"))
        # st.pyplot()


    if choices == "Predicting Bumble Bee Species Count":
        st.subheader("Flower Plants That Are Relatively Important to Bumble Bee Species Richness According to Estimated Model")

        plant_pics = Image.open("images/beelovingplants.png")
        st.image(plant_pics)

        st.subheader("Predict The Expected BumbleBee Species Diversity From Flower Plants and Climate Variables")
        county =st.selectbox("select County", tuple(county_label.keys()))
        temperature =st.number_input("Select Average Temperature", -20.0, 50.0) # 2 min and 10 max
        wind_gust =st.number_input("Select Average Wind Gust", 0.0, 200.0) # 2 min and 10 max
        precipitation =st.number_input("Select Average Precipitation", 0.0, 100.0) # 2 min and 10 max
        plant_Achillea = st.selectbox("select Achillea sp. or Not Achillea sp.", tuple(Achillea_label.keys()))
        plant_Asteraceae = st.selectbox("select Asteraceae sp. or Not Asteraceae", tuple(Asteraceae_label.keys()))
        plant_Brassica = st.selectbox("select Brassica sp. or Not Brassica", tuple(Brassica_label.keys()))
        plant_Cirsium = st.selectbox("select Cirsium sp. or Not Cirsium", tuple(Cirsium_label.keys()))
        plant_Delphinium = st.selectbox("select Delphinium sp. or Not Delphinium", tuple(Delphinium_label.keys()))
        plant_Epilobium_latifolium = st.selectbox("select Epilobium latifolium or Not Epilobium latifolium", tuple(Epilobium_label.keys()))
        plant_Erigeron = st.selectbox("select Erigeron sp. or Not Erigeron", tuple(Erigeron_label.keys()))
        plant_Lathyrus = st.selectbox("select Lathyrus sp. ot Not Lathyrus", tuple(Lathyrus_label.keys()))
        plant_Lotus_corniculatus = st.selectbox("select corniculatus sp. or Not corniculatus", tuple(Lotus_label.keys()))
        plant_Phacelia = st.selectbox("select Phacelia sp. or Not Phacelia", tuple(Phacelia_label.keys()))
        plant_Robus_allegheniensis = st.selectbox("select Robus allegheniensis or Not Robus allegheniensis", tuple(Rubus_label.keys()))
        plant_Scrophularia = st.selectbox("select Scrophularia sp. or Not Scrophularia", tuple(Scrophularia_label.keys()))

        #Encoding: user selects something but how do we get it in a form ml can accept: basicaly the values

        v_county = get_values(county, county_label)
        v_plant_Achillea = get_values(plant_Achillea, Achillea_label)
        v_plant_Asteraceae = get_values(plant_Asteraceae, Asteraceae_label)
        v_plant_Brassica = get_values(plant_Brassica, Brassica_label)
        v_plant_Cirsium = get_values(plant_Cirsium, Cirsium_label)
        v_plant_Delphinium = get_values(plant_Delphinium, Delphinium_label)
        v_plant_Epilobium_latifolium = get_values(plant_Epilobium_latifolium, Epilobium_label)
        v_plant_Erigeron = get_values(plant_Erigeron, Erigeron_label)
        v_plant_Lathyrus = get_values(plant_Lathyrus, Lathyrus_label)
        v_plant_Lotus_corniculatus = get_values(plant_Lotus_corniculatus, Lotus_label)
        v_plant_Phacelia = get_values(plant_Phacelia, Phacelia_label)
        v_plant_Robus_allegheniensis = get_values(plant_Robus_allegheniensis, Rubus_label)
        v_plant_Scrophularia = get_values(plant_Scrophularia, Scrophularia_label)


        #pretty_data shows the user what the ml will use: is that neccessary?
        pretty_data = {
        "county": county,
        "temperature": temperature,
        "wind_gust" : wind_gust,
        "precipitation": precipitation,
        "plant_Achillea sp." : plant_Achillea, 
        "plant_Asteraceae sp.": plant_Asteraceae,
        "plant_Brassica sp." : plant_Brassica,
        "plant_Cirsium sp." : plant_Cirsium, 
        "plant_Delphinium sp." : plant_Delphinium,
        "plant_Epilobium latifolium" : plant_Epilobium_latifolium,
        "plant_Erigeron sp." : plant_Erigeron, 
        "plant_Lathyrus sp." : plant_Lathyrus, 
        "plant_Lotus corniculatus" : plant_Lotus_corniculatus, 
        "plant_Phacelia sp." : plant_Phacelia,
        "plant_Robus allegheniensis" : plant_Robus_allegheniensis,
        "plant_Scrophularia sp." :plant_Scrophularia,  
        }

        sample_data= [v_county, temperature, wind_gust, precipitation, v_plant_Achillea, v_plant_Asteraceae, 
                      v_plant_Brassica, v_plant_Cirsium, v_plant_Delphinium,  v_plant_Epilobium_latifolium,
                      v_plant_Erigeron, v_plant_Lathyrus, v_plant_Lotus_corniculatus, v_plant_Phacelia, 
                      v_plant_Robus_allegheniensis, v_plant_Scrophularia]

        prepro_data = preprocessing.scale(sample_data)
        
        prep_data = np.array( prepro_data).reshape(1,-1) #shape data into 2d

        predictor = joblib.load("models/poisson_tree.pkl")
        #load_prediction_model("models/poisson_tree.pkl")
        prediction = predictor.predict(prep_data) #reshape sample into 2 d for it towork


        final_result = (prediction)
        st.success(final_result)

if __name__ == "__main__":
    main()