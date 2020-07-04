import streamlit as st
import datetime
from PIL import Image

# Text/Title
st.title("Streamlit Tutorials")

# Header
st.header("This is a header")

# Subheader
st.subheader("This is Sub Header")

# Text
st.text("Hello Streamlit")

# Markdown
st.markdown("### This is a __'MARKDOWN'__")

# Error/Colorful text
st.success("Successful")

st.info("Information")

st.warning("Warning")

st.error("Error")

st.exception("NLP ('Import Error')")

# Get Help Info About Python
st.help(range)

# Writing Text
st.write("Text with write")
st.write(range(10))

# Images

img = Image.open("../data/test_images/bhp.jpg")
st.image(img, width=300, caption="Simple Image")

# Videos
vid_file = open("../data/test_videos/Losing my life - Falling in reverse(LIVE).mp4", "rb").read()
st.video(vid_file)

# Audio
audio_file = open("../data/audio_files/High End - Confidential 320Kbps.mp3", "rb").read()
st.audio(audio_file, format='audio/mp3')

# Widgets
## Checkbox
if st.checkbox("Show/hide"):
    st.text("Who are you!!!")

## Radio Buttons
status = st.radio("What is your status", ("Active", "Inactive"))

if status == "Active":
    st.success("You are Active")
else:
    st.warning("Inactive")

# Select Box
occupation = st.selectbox("Your Occupation", ["Programmer", "Data Engineer", "Doctor"])
st.write("You Selected: ", occupation)

# Multi Select
location = st.multiselect("Where do yo work?", ["Chennai", "Bangalore", "Pune", "Hydrabad"])
st.write("You work at: ", len(location), "locations")

# Slider
level = st.slider("What is your level in R6", 1, 400)
st.write("Your level: ", level)

# Butons
st.button("Simple Button")

about = st.button("About")
if about:
    st.text("Streamlit is COOL!!")

# Text input
name = st.text_input("Enter your Name", "type here...")

if st.button("Submit", key="text_input"):
    result = name.title()
    st.success(result)

# Text Area

message = st.text_area("Enter your Message", "Type Here...")

if st.button("Submit", key="text_area"):
    result = message.title()
    st.success(result)

# Date input
today = st.date_input("Today is ", datetime.datetime.now())

# Time
time = st.time_input("Time: ", datetime.time())

# Display JSON
st.text("Display JSON")
bio = st.json({"name": "basotra",
               "age": 22,
               "gender": "male"
               })
# Display Raw Code
st.text("Display Raw Code")
st.code("import numpy as np")

with st.echo():
    # this is comment
    import pandas as pd
    import matplotlib.pyplot as plt

    df = pd.DataFrame()

# Progress Bar
my_bar = st.progress(0)

for p in range(10):
    my_bar.progress(p + 1)

# Spinner
import time

with st.spinner("Waiting..."):
    time.sleep(5)
st.success("Finished!")

# Ballons
# st.balloons()

# Side Bar
st.sidebar.header("About")
st.sidebar.text("This is Streamlit")


# Functions
@st.cache # to make it run faster
def func():
    return range(100)


if st.button("Range [1- 100]"):
    st.write(func())

# Plot
st.pyplot()

# DataFrames
st.dataframe(df)

# Tables
st.table(df)
