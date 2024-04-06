import streamlit as st

st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", width=400)

with col2:
    st.title("Sandeep Gajbi")
    content = """ Hi, I am Sandeep! I am a Python programmer. """
    st.info(content)
