
# def fetch_poster(movie_title):
#     url = f"https://www.omdbapi.com/?t={movie_title}&apikey=b5b4bd76"
#     data = requests.get(url)
#     data = data.json()
#     if data['Response'] == 'True':
#         return data['Poster']
#     else:
#         return "Poster not found"
import streamlit as st
import pickle
import requests

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path

movies = pickle.load(open("movieL.pkl", 'rb'))
simi = pickle.load(open("simi.pkl", 'rb'))
MovieL = movies['title'].values

st.set_page_config(page_title="Movie Recommender System", layout="centered")
st.header("Select your favorite movie 🐼!")

selectvalue = st.selectbox("", MovieL)

# def recommend(movie):
#     index = movies[movies['title'] == movie].index[0]
#     distance = sorted(list(enumerate(simi[index])), reverse=True, key=lambda vector: vector[1])
#     recommend_movie = []
#     recommend_poster = []
#     for i in distance[1:6]:  
#         recommend_movie.append(movies.iloc[i[0]].title)
#         recommend_poster.append(fetch_poster(movies.iloc[i[0]].title))
#     return recommend_movie, recommend_poster

def recommend(movie):
    index=movies[movies['title']==movie].index[0]
    distance = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda vector:vector[1])
    recommend_movie=[]
    recommend_poster=[]
    for i in distance[1:6]:
        movies_id=movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        recommend_poster.append(fetch_poster(movies_id))
    return recommend_movie, recommend_poster

if st.button("Show Recommendations"):
    movie_name, movie_poster = recommend(selectvalue)
    
    cols = st.columns(5)
    for i in range(5):
        with cols[i]:
            st.image(movie_poster[i], use_column_width=True, caption=movie_name[i])
            st.write("")

st.markdown(
    """
    <style>
        * {
            border-color: #12e9b3 !important;
        }
        body {
            background-color: #121212;
            color: #ffffff;
            height: 100vh;
            gap: 20px;
            text-align: center;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-family: 'Arial', sans-serif;
        }
        .stImage > div > div > p {
            color: black;
            font-weight: bold;
            margin-top: 5px;
        }
        .stSelectbox {
            margin: 0;
        }
        h1 {
            color: #444444;
            font-weight: bold;
        }
        h2 {
            font-size: 4em;
            color: #444444;
        }
        .stApp {
            display: flex;
            justify-content: center;
            align-items: center;
            color: #121212;
            background-color: #ffffff;
        }
        .stAppHeader {
            color: #ffffff;
            background-color: #14151a;
        }
        .stMainBlockContainer {
            min-height: 100vh;
            display: flex;
            justify-content: center;
        }
        .stMainBlockContainer div {
            justify-content: center;
        }
        .stHorizontalBlock {
            width: 100%;
            justify-content: center;
            align-items: center;
            display: flex;
        }
        select {
            background-color: #e6e6e6;
            color: #fff;
            padding: 10px;
            border: none;
        }
        p {
            color: #121212;
            transition: 0.3s ease-in-out;
        }
        .stButton > button {
            margin-top: 20px;
            border: 1px solid rgb(43, 43, 43);
            background-color: #ffffff;
            color: white;
            padding: 10px 20px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            transition: 0.3s ease-in-out;
        }
        .stButton > button:hover {
            box-shadow: 0 0 20px #0df0f8; 
            border: 1px solid rgb(15, 250, 160);
            background-color: #0fe97c; 
        }
        .stButton > button:focus {
            box-shadow: 0 0 20px #0df0f8; 
            border: 1px solid rgb(15, 250, 160) !important;
            background-color: #0fe97c; 
            outline: none;
        }
        .stButton > button:hover p {
            color: white;
        }
        .stColumn {
            min-width: 200px;
            max-width: 250px;
        }
        .stImage {
            overflow: hidden;
            box-sizing: border-box;
            color: black !important;
            border-radius: 5px;
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.623);
        }
        .stImage div div {
            font-weight: bold;
            font-size: 16px;
            color: rgb(85, 85, 85);
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.write("Using OMDB Api. Project by Nitin Sharma")
