import streamlit as st
from PIL import Image, ImageOps

st.title("Title")
st.caption("これはテストアプリです♪")

# image=Image.open("./data/画像01.jpg")
# st.image(image,width=200)

with open("./data/Popping-popcorn.gif", "rb") as f:
    st.image("./data/Popping-popcorn.gif", caption="Popcorn", use_container_width=True)