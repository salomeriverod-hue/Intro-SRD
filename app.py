import streamlit as st
st.title ("Mi primera app")
st.header ("Esta página está dedicada a mi")
from PIL import Image
image = Image.open ("samicalvo.jpeg")
st.image(image, caption= "este es sami")
texto = st.text_input("Ingresa texto", "texto inicial")
st.write("El texto que has escrito es", texto)
