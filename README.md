# 🎬 Movie Recommendation System

A content-based movie recommender web app that suggests 5 similar movies based on a movie you select, complete with poster images fetched live from The Movie Database (TMDB) API.

## 🚀 Features

- Recommends top 5 similar movies based on content similarity (genres, keywords, cast, crew, and overview)
- Fetches real-time movie posters using the TMDB API
- Simple, interactive web interface built with Streamlit
- Dropdown search to select any movie from the dataset

## 🛠️ Built With

- **Python**
- **Pandas** – data preprocessing and manipulation
- **Scikit-learn** – text vectorization (CountVectorizer) and cosine similarity
- **NLTK** – text stemming
- **Streamlit** – web app framework
- **TMDB API** – fetching movie posters
- **Pickle** – model/data serialization

## 📊 Dataset

This project uses the **[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)**, which includes metadata for 5,000 movies such as genres, keywords, cast, crew, and overview.

## ⚙️ How It Works

1. Movie metadata (genres, keywords, cast, crew, overview) is combined into a single "tags" feature for each movie
2. Text is vectorized using `CountVectorizer` and stemmed using NLTK's `PorterStemmer`
3. Cosine similarity is computed between all movie vectors
4. When a user selects a movie, the 5 most similar movies (by cosine similarity score) are returned
5. Posters for the recommended movies are fetched dynamically via the TMDB API

## 📦 Installation

```bash
git clone https://github.com/your-username/MovieRecommendationSystem.git
cd MovieRecommendationSystem
python -m venv .venv
.venv\Scripts\activate
python -m pip install -r requirements.txt
```

## ▶️ Usage

```bash
streamlit run app.py
```

## 🔑 API Key

This project requires a TMDB API key to fetch movie posters. Get one for free at [themoviedb.org](https://www.themoviedb.org/settings/api) and add it to `app.py`.

## 📸 Demo

*(Add a screenshot or GIF of your app here)*

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
