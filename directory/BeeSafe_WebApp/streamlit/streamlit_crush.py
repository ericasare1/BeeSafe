import streamlit as st


#test/title

st.title("Streamlit Tutorials")

#header/subheader
st.header("This is a header")
st.subheader("this is a subheader")

#test
st.text("hell0 olen")

#markdown
st.markdown("### this is a markdown")

#error/colour text
st.success("successful")
st.info("information")
st.warning("this is a warning")
st.error("this is an error")
st.exception("Nameerror('name three not defined")

#get help
st.help(range)

#writing test
st.write("Test with write")

st.write(range(10))

#images
from Pil import image
img =Image.open("example.jpeg")
st.image(img, width=300, caption= "Simple Image")

#videos
vid_file = open("example.mp4", "rb")
vid_bytes = vid_file.read()
st.video(vid_file)

#audio
audio_file = open("examplemusic.mp3", "rb").read
st.audio(audio_file, format="audio/mp3")


#widget
#checkbox

if st.checkbox("show/hide"):
    st.text("showinh or Hiding widget")

#radio buttons
status =st.radio("what is your status", ("Active", "Inactive"))

if status == "Active":
    st.success("you are active")
else:
    st.warning("Inactive, Activate")

#Select box
occupation = st.selectbox("your occupation", ["programmer", "data scientist", "doctor", "businessman"])
st.write("your selected this optiom", occupation)



#multi Select
location = st.multiselect("where do you work?", ("london", "new york", "accra", "kiev", "nepal"))
st.write("you selected ", len(location), "locaions")

#slider
level = st.slider("what is your level", 1,5)

#Buttons
st.button("simple button")
if st.button("about"):
    st.text("streamlit is cool")

#test input
firstname= st.test_input("Enter your firstname", "type here..")
if st.button("submit"):
    result = firstname.title()
    st.sucess(result)

#test Area
firstname= st.test_area("Enter your firstname", "type here..")
if st.button("submit"):
    result = message.title()
    st.sucess(result)

#Date input
import datetime
today = st.date_input("Today is ", datetime.datetime.now())

#time\
the_time =  st.time_input("The time is", datetime.time())

#displaying json
st.text("Display JSON")
st.json({"Name" : "Jesses", 'gender': 'male'})

#display raw code
st.text('display raw code')
st.code("import numpy as np")

#display raw code 
with st.echo(): #will also show comment
    import pandas as pd
    df = pd.DataFrame()

#progress bar
import time
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p+1)

#spinner
with st.spinner('waiting ..'):
    time.sleep(5)
st.success("finished")

#Ballons
st.balloons()

#Sidebars
st.sidebar.header("about")
st.sidebar.text("this is a streamlit tutorial")

#functions
@st.cache
def run_fxn():
    return range(100)

st.write(run_fxn())

#plotting
st.pyplot()

#dataframes
st.DataFrame(df)

#tables
st.table(df)



