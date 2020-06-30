#core pkgs
import streamlit as st
import os
import joblib
from PIL import Image

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

#dictionary to get all the variables and encoding to be used in selectbox
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
plant_label = {'Grindelia stricta': 0, 'Geranium sp.': 1, 'Solidago velutina': 2, 'Digitalis purpurea': 3, 'Erigeron sp.': 4, 'Trifolium pratense': 5,
                'Lathyrus sp.': 6, 'Penstemon sp. (purple)': 7, 'Dodecatheon alpinum': 8, 'Rubus parviflorus': 9, 'Lathyrus odoratus': 10,
                'Pedicularis labradorica': 11, 'Trifolium repens': 12, 'Achillea sp.': 13, 'Rubus allegheniensis': 14, 'Eupatorium sp.': 15,
                'Lupinus arboreus': 16, 'Agastache sp.': 17, 'Epilobium parviflorum': 18, 'Cleome sp.': 19, 'Trifolium sp.': 20,
                 'Rudbeckia occidentalis': 21, 'Scrophularia sp.': 22, 'Dalea candida var.oligophylla': 23, 'Liatris sp.': 24, 'Astragalus sp.': 25,
                 'Melilotus officinalis': 26, 'Chrysothamnus nauseosus ssp.arenarius': 27, 'Monarda fistulosa': 28, 'Antennaria sp.': 29,
                 'Centaurea sp.': 30, 'Centaurea cyanus': 31, 'Marrubium sp.': 32, 'Epilobium latifolium': 33, 'Rudbeckia sp.': 34,
                 'Malvaceae sp.': 35, 'Senecio multicapitatus': 36, 'Epilobium angustifolium': 37, 'Heracleum sp.': 38, 'Brassica sp.': 39,
                 'Grindelia sp.': 40, 'Taraxacum officinale': 41, 'Asteraceae sp.': 42, 'Rubus discolor': 43, 'Rubus sp.': 44,
                'Eriogonum sp.': 45, 'Hypericum perforatum': 46, 'Cirsium arvense': 47, 'Phacelia sp.': 48, 'Helichrysum sp.': 49,
                'Linaria vulgaris': 50, 'Campanula sp.': 51, 'Epilobium sp.': 52, 'Verbascum thapsus': 53, 'Cirsium sp.': 54,
                'Delphinium sp.': 55, 'Pedicularis sp.': 56, 'Rudbeckia laciniata': 57, 'Mertensia sp.': 58, 'Lupinus sp.': 59,
                 'Penstemon sp.': 60, 'Tilia sp.': 61, 'Ceanothus sp.': 62, 'Solidago sp.': 63, 'Stachys sp.': 64, 'Allium sp.': 65,
                 'Aster sp.': 66, 'Senecio sp.': 67, 'Potentilla sp.': 68, 'Medicago sativa': 69,'Lotus corniculatus': 70,
                 'Bellis sp.': 71, 'Symphoricarpos albus': 72, 'Spiraea douglasii': 73, 'Melilotus sp.': 74, 'Chrysothamnus sp.': 75,
                 'Zigadenus sp.': 76, 'Prunella sp.': 77, 'Melilotus alba': 78, 'Withheld': 79, 'Rosa sp.': 80,
                'Monarda sp.': 81, 'Monardella sp.': 82, 'Vicia sp.': 83}

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
        st.subheader("Predict The Expected BumbleBee Species Diversity From Flower Plants and Climate Variables")

        plant = st.selectbox("Select Plant Type", tuple(plant_label.keys())) # and choose options to select: go up and create a dictionary and use tuple to convert keys into list so user can see
        county =st.selectbox("select County", tuple(county_label.keys()))
        temperature =st.number_input("Select Average Temperature", -20.0, 50.0) # 2 min and 10 max
        precipitation =st.number_input("Select Average Precipitation", 0.0, 100.0) # 2 min and 10 max


        #Encoding: user selects something but how do we get it inform ml can accept: basicaly the values

        v_plant = get_values(plant, plant_label)
        v_county = get_values(county, county_label)

        #pretty_data shows the user what the ml will use: is that neccessary?
        pretty_data = {
        "plant": plant,
        "county": county,
        "temperature": temperature,
        "precipitation": precipitation,
        }

        sample_data= [v_plant, v_county, temperature, precipitation]  

        prep_data = np.array(sample_data).reshape(1,-1) #shape data into 2d

        predictor = joblib.load("models/lasso_bee_model.pkl")
        #load_prediction_model("models/lasso_bee_model.pkl")
        prediction = predictor.predict(prep_data) #reshape sample into 2 d for it towork


        final_result = (prediction)
        st.success(final_result)

if __name__ == "__main__":
    main()