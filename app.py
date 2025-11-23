import streamlit as st
import pickle
import requests

# Load dataframe
movies_df = pickle.load(open('movies.pkl', 'rb'))
movies_list = movies_df['title'].values

similarity = pickle.load(open('similarity.pkl', 'rb'))

API_KEY = "bcfa936bb4d7ff44b5d3aacfc44c7abb"

def fetch_poster(movie_title):
    try:
        url = f"https://api.themoviedb.org/3/search/movie?api_key={API_KEY}&query={movie_title}"
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, headers=headers)
        data = response.json()

        if "results" not in data or len(data["results"]) == 0:
            return "https://via.placeholder.com/500x750.png?text=No+Poster"

        movie_data = data["results"][0]

        if movie_data.get("poster_path") is None:
            return "https://via.placeholder.com/500x750.png?text=No+Poster"

        poster_path = movie_data["poster_path"]
        return "https://image.tmdb.org/t/p/w500" + poster_path

    except Exception as e:
        return "https://via.placeholder.com/500x750.png?text=Error"


def recommend(movie):
    movie_index = movies_df[movies_df['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_sorted = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []

    for i in movies_sorted:
        title = movies_df.iloc[i[0]].title
        recommended_movies.append(title)

        poster = fetch_poster(title)
        recommended_posters.append(poster)

    return recommended_movies, recommended_posters


st.title('HybridLens Movie Recommender')

selected_movie_name = st.selectbox(
    "Which movie do you want to watch?",
    movies_list
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)

    cols = st.columns(5)

    for i in range(5):
        with cols[i]:
            st.text(names[i])
            st.image(posters[i])
