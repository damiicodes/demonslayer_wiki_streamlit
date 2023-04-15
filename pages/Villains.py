import streamlit as st
import pandas

st.set_page_config(layout='wide')

with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


df = pandas.read_csv('/Users/damifajinmi/demonslayer_wiki_streamlit/demons.csv', sep=',')

st.title('Demon Slayer Wiki')
st.image('images/mainvillain.png')


col1 = st.container()
col2, empty_col, col3 = st.columns([1.5, 0.5, 1.5])


with col1:
    st.write('<p2> Below is a list of characters that appear in the Demon Slayer Anime </p2>',
             unsafe_allow_html=True)

with col2:
    for index, row in df[:4].iterrows():
        st.header(row['character name'])
        st.write('<p3>' + row['description'] + '</p3>', unsafe_allow_html=True)
        st.image('images/' + row['image'], width=400)
        st.write('Episode Appearances:' + " " + row['episode appearance'])

with col3:
    for index, row in df[4:].iterrows():
        st.header(row['character name'])
        st.write('<p3>' + row['description'] + '</p3>', unsafe_allow_html=True)
        st.image('images/' + row['image'], width=400)
        st.write('Episode Appearances:' + " " + row['episode appearance'])