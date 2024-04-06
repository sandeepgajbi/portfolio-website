import pandas
import streamlit as st
import pandas

content = """ Welcome to my portfolio! I'm Sandeep, an experienced business analyst venturing into the exciting world of development. With a rich background in analyzing complex business processes and identifying opportunities for growth, I bring a unique perspective to my journey as a developer.

While my roots lie in business analysis, my passion for technology has led me to delve into Python development. Embracing this new challenge, I'm dedicated to honing my skills and mastering the art of crafting elegant and efficient solutions through code.

Driven by a curiosity to explore new avenues and expand my expertise, I'm committed to continuous learning and pushing the boundaries of what's possible. My transition from business analysis to development represents my adaptability and eagerness to embrace new challenges head-on.

Join me on this exciting journey as I showcase my evolving skills and the projects I'm passionate about. From leveraging data to drive strategic decisions to building innovative Python applications, I'm eager to make an impact and create value in both the business and tech realms.

Let's connect and collaborate to bring your ideas to life with creativity, insight, and technical expertise! """

content_1 = """
Below you can find some of the apps I have built in Python.
"""
st.set_page_config(layout="wide")
col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.jpg", use_column_width="auto", output_format="auto")

with col2:
    st.title("Sandeep Gajbi")
    st.info(content)

st.subheader(content_1)

col3, empty_col, col4 = st.columns([1.5, 0.5, 1.5])

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/" + row["image"])
        st.write(f"[Source Code]({row['url']})")

