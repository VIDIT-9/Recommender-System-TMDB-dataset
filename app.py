import streamlit as st
import pickle
import pandas as pd
import requests

def Fetch_Poster(Movie_ID):
    response = requests.get('https://api.themoviedb.org/3/movie/{}?api_key=412d4a92b67f012377a5a9a786c86e75&language=en-US'.format(Movie_ID))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


def recommend(movie_name):
    index = Movies[Movies['title'] == movie_name].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key = lambda x: x[1])

    Recommended_Movies = []
    Recommended_Movies_Poster = []
    for itr in distances[1:6]:

        Movie_ID = Movies.iloc[itr[0]]['movie_id']

        Recommended_Movies.append(Movies.iloc[itr[0]].title)
        Recommended_Movies_Poster.append(Fetch_Poster(Movie_ID))

    return Recommended_Movies, Recommended_Movies_Poster


st.title('Movie Recommendation System')

MoviesDict = pickle.load(open('AllMovies.pkl', 'rb'))
Movies = pd.DataFrame(MoviesDict)

similarity = pickle.load(open('SimilarityMatrix.pkl', 'rb'))


selected_movie = st.selectbox(
    'Looking for a good movie, we will get it for you',
    Movies['title'].values)

if st.button('Recommend'):
    Recommendations, Posters = recommend(selected_movie)

    movie1, movie2, movie3, movie4, movie5 = st.columns(5)

    with movie1:
        st.text(Recommendations[0])
        st.image(Posters[0])

    with movie2:
        st.text(Recommendations[1])
        st.image(Posters[1])

    with movie3:
        st.text(Recommendations[2])
        st.image(Posters[2])

    with movie4:
        st.text(Recommendations[3])
        st.image(Posters[3])

    with movie5:
        st.text(Recommendations[4])
        st.image(Posters[4])


