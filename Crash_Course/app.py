import streamlit as st

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
from PIL import Image
img = Image.open("..\data\\test_images\\bhp.jpg")
st.image(img, width=300, caption="Simple Image")

# Videos
vid_file = open("../data//test_videos//celebrity_FR.mp4", "rb").read()
st.video(vid_file)

# Audio
audio_file = open("")