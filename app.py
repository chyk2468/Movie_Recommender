import pickle
import streamlit as st
import requests
import pandas as pd

def get_movie_details(movie_id, movie_details_dict):
    """Gets movie details from local data."""
    try:
        # Get details from local CSV data
        details = movie_details_dict.get(movie_id, {})
        
        # Extract year from release_date
        release_date = details.get('release_date', '')
        year = release_date.split('-')[0] if release_date and release_date != 'nan' else 'N/A'
        
        # Get rating
        rating = details.get('vote_average', 0.0)
        if pd.isna(rating):
            rating = 0.0
        
        # Use placeholder poster since we're not using API
        poster_url = "https://placehold.co/500x750/333/FFFFFF?text=Movie+Poster"
        
        return poster_url, year, rating
    except Exception as e:
        st.error(f"Error getting movie details: {e}")
        return "https://placehold.co/500x750/333/FFFFFF?text=No+Poster", "N/A", 0.0


def recommend(movie):
    """Recommends 5 similar movies based on the selected movie."""
    try:
        index = movies[movies['title'] == movie].index[0]
    except IndexError:
        st.error("Movie not found in the dataset. Please select another one.")
        return [], [], [], []
        
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    
    recommended_movie_names = []
    recommended_movie_posters = []
    recommended_movie_years = []
    recommended_movie_ratings = []

    for i in distances[1:6]:
        # get the movie details from local data
        movie_id = movies.iloc[i[0]].movie_id
        
        poster_url, year, rating = get_movie_details(movie_id, movie_details)
        recommended_movie_posters.append(poster_url)
        recommended_movie_names.append(movies.iloc[i[0]].title)
        recommended_movie_years.append(year)
        recommended_movie_ratings.append(rating)

    return recommended_movie_names, recommended_movie_posters, recommended_movie_years, recommended_movie_ratings


st.set_page_config(layout="wide")
st.header('Movie Recommender System Using Machine Learning')
try:
    movies_dict = pickle.load(open('movies.pkl', 'rb'))
    movies = pd.DataFrame(movies_dict)
    similarity = pickle.load(open('similarity.pkl', 'rb'))
    
    # Load original CSV data for additional movie information
    movies_csv = pd.read_csv('tmdb_5000_movies.csv')
    # Create a mapping from movie_id to additional details
    movie_details = movies_csv.set_index('id')[['title', 'release_date', 'vote_average']].to_dict('index')
    
except FileNotFoundError:
    st.error("Model files not found. Please run the data processing notebook first.")
    st.stop()


movie_list = movies['title'].values
selected_movie = st.selectbox(
    "Type or select a movie from the dropdown",
    movie_list
)

if st.button('Show Recommendation'):
    with st.spinner('Finding recommendations...'):
        recommended_movie_names, recommended_movie_posters, recommended_movie_years, recommended_movie_ratings = recommend(selected_movie)
    
    if recommended_movie_names:
        cols = st.columns(5)
        for i, col in enumerate(cols):
            with col:
                st.text(recommended_movie_names[i])
                st.image(recommended_movie_posters[i])
                # Display year
                year = recommended_movie_years[i]
                st.caption(f"Year: {year}")
                
                rating = recommended_movie_ratings[i]
                st.caption(f"Rating: {rating:.1f} ⭐")