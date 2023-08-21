import streamlit as st
import pickle
import pandas as pd


def recommend(movie_name):
    index = Movies[Movies['title'] == movie_name].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key = lambda x: x[1])

    RecommendedMovies = []
    for itr in distances[1:6]:

        # Fetch Poster using Movie_ID from API
        Movie_ID = Movies.iloc[itr[0]]['movie_id']

        RecommendedMovies.append(Movies.iloc[itr[0]].title)
    return RecommendedMovies


st.title('Movie Recommendation System')

MoviesDict = pickle.load(open('AllMovies.pkl', 'rb'))
Movies = pd.DataFrame(MoviesDict)

similarity = pickle.load(open('SimilarityMatrix.pkl', 'rb'))


selected_movie = st.selectbox(
    'Looking for a good movie, we will get it for you',
    Movies['title'].values)

if st.button('Recommend'):
    Recommendations = recommend(selected_movie)
    for movie in Recommendations:
        st.write(movie)