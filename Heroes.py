import streamlit as st
import pandas

st.set_page_config(layout='wide')

with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


df = pandas.read_csv('demonslayers.csv', sep=',')


st.title('Demon Slayer Wiki')

col1, col2 = st.columns([1, 3])
col3 = st.container()
col4 = st.container()
col5, empty_col, col6 = st.columns([1.5, 0.5, 1.5])

with col1:
    st.image('images/logo.png')


with col2:
    st.image('images/mixedchar.png', width=400)

with col3:
    with open('show_description.txt') as file:
        content = file.read()
        st.info(content)


with col4:
    st.write('<p2> Below is a list of characters that appear in the Demon Slayer Anime </p2>',
             unsafe_allow_html=True)

with col5:
    for index, row in df[:6].iterrows():
        st.header(row['character name'])
        st.write('<p3>' + row['description'] + '</p3>', unsafe_allow_html=True)
        st.image('images/' + row['image'], width=400)
        st.write('Episode Appearances:' + " " + row['episode appearance'])

with col6:
    for index, row in df[6:].iterrows():
        st.header(row['character name'])
        st.write('<p3>' + row['description'] + '</p3>', unsafe_allow_html=True)
        st.image('images/' + row['image'], width=400)
        st.write('Episode Appearances:' + " " + row['episode appearance'])
