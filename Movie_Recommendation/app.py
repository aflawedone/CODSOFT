import pandas as pd
import streamlit as st
import pandas
import pickle

def recommend(movies):
    movie_index = movie_store[movie_store['Series_Title'] == movies].index[0]
    distances = similarities[movie_index]
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    for i in movie_list:
        recommended_movies.append(movie_store.iloc[i[0]].Series_Title)
    return recommended_movies


st.header("MOVIE RECOMMENDATION SYSTEM")

movies_df = pickle.load(open('Backend_System/movie_list.pkl', 'rb'))
similarities = pickle.load(open('Backend_System/similarity.pkl', 'rb'))

movie_store = pd.DataFrame(movies_df)

selected_movie_name = st.selectbox(
    'Select a movie to get recommended for more',
    movie_store['Series_Title'].values)

if st.button('Recommend'):
    rec = recommend(selected_movie_name)
    for i in rec:
        st.write(i)
