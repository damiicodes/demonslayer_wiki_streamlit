import streamlit as st
import pandas

st.title('Demon Slayer Wiki')

col1, col2 = st.columns([1, 3])
col3 = st.container()
col4 = st.container()

with col1:
    st.image('images/logo.png')


with col2:
    st.image('images/mixedchar.png', width=400)

with col3:
    with open('show_description.txt') as file:
        content = file.read()
        st.info(content)


with col4:
    st.write('<p> Below is a list of characters that appear in the Demon Slayer Anime </p>',
             unsafe_allow_html=True)
