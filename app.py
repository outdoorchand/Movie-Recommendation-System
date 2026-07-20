import pickle
import requests
import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)

TMDB_API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

# Load data once at startup
movies_list = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open('similarity.pkl', 'rb'))


def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US".format(
        movie_id, TMDB_API_KEY
    )
    try:
        response = requests.get(url, timeout=5)
        data = response.json()
        poster_path = data.get('poster_path')
        if poster_path:
            return "https://image.tmdb.org/t/p/w500/" + poster_path
    except requests.RequestException:
        pass
    # Fallback placeholder if TMDB call fails or poster is missing
    return "https://via.placeholder.com/500x750?text=No+Image"


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_ranked = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []
    recommended_posters = []
    for i in movies_ranked:
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


@app.route('/', methods=['GET', 'POST'])
def index():
    all_titles = movies['title'].values
    recommendations = None
    selected_movie = None

    if request.method == 'POST':
        selected_movie = request.form.get('movie')
        if selected_movie in all_titles:
            names, posters = recommend(selected_movie)
            recommendations = list(zip(names, posters))

    return render_template(
        'index.html',
        titles=all_titles,
        recommendations=recommendations,
        selected_movie=selected_movie
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)