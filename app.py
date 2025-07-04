from PIL import Image

import requests
import streamlit as st





st.set_page_config(page_title="HELLO WORLD" , page_icon="ChatGPT Image Mar 31, 2025, 04_09_22 PM.png",layout="wide")
#-----ANIMATION-----


img = Image.open("ChatGPT Image Mar 31, 2025, 04_09_22 PM.png")
# HEADER PART # ---
with st.container():
    st.title("A student learning python")
    st.header("HI I AM MANAV :smiley:")
    st.write("nkfirhuhfohfiegfgseigiu")
    st.write("[to learn more >](https://youtube.com)")

with st.container():
    st.write("---")
    left_column , right_column  =st.columns(2)
    with left_column :
        st.header("WHT DO I DO ")
 

with st.container():
    st.write("---")
    image_column , text_coloumn = st.columns((1000,3000))
    with image_column:
        st.image(img)
    with text_coloumn:
        st.markdown("<h1 style='font-size: 100px;'>SO HERE WE GO AGAIN </h1>", unsafe_allow_html=True)
