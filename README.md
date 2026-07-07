# 🎬 Movie Recommendation System

A content-based movie recommender web app that suggests 5 similar movies based on a movie you select, complete with poster images fetched live from The Movie Database (TMDB) API.

Step 1: You will first download the data set, from Kaggle the link is given here. It is also given in the my repositry.
Link: https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata

Step 2: After this you upload the data set into the jupyter notebook. 

Step 3: In this step you run the "DataProcessingForMoviesRecommendationSystem.ipynb" step by step

Step 4: Then you got two pkl files in the jupyter "Home". 
-----> 1."movie_dict.pkl" 
-----> 2."simularity.pkl"

Step 5: Make a project folder on the pycharm or a folder on any path in your computer.

Step 6: Make a file name is app.py then run it code is given in app file.

Step 7: Run requirements.txt in vitual environment ".venv\Scripts\activate"



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

This project uses the **[TMDB 5000 Movie Dataset](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)** from Kaggle, which includes metadata for 5,000 movies such as genres, keywords, cast, crew, and overview. The dataset is also included in this repository.

## ⚙️ How It Works

1. Movie metadata (genres, keywords, cast, crew, overview) is combined into a single "tags" feature for each movie
2. Text is vectorized using `CountVectorizer` and stemmed using NLTK's `PorterStemmer`
3. Cosine similarity is computed between all movie vectors
4. When a user selects a movie, the 5 most similar movies (by cosine similarity score) are returned
5. Posters for the recommended movies are fetched dynamically via the TMDB API

## 📦 Setup & Installation

### Step 1: Download the dataset
Download the TMDB 5000 Movie Dataset from Kaggle (also included in this repository):
👉 [https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

### Step 2: Load the dataset into Jupyter Notebook
Upload the dataset CSV files into your Jupyter Notebook environment.

### Step 3: Run the data processing notebook
Open and run `DataProcessingForMoviesRecommendationSystem.ipynb` step by step from top to bottom.

### Step 4: Generate the model files
After running the notebook, two `.pkl` files will be generated in your Jupyter "Home" directory:
- `movie_dict.pkl`
- `similarity.pkl`

### Step 5: Create your project folder
Create a new project folder (e.g., in PyCharm, or anywhere on your computer), and place `app.py` along with the two `.pkl` files from Step 4 inside it.

### Step 6: Add the app code
Create `app.py` in the project folder and add the app code (included in this repository).

### Step 7: Set up a virtual environment and install dependencies

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

## ▶️ Usage

Once everything is set up, run the app with:

```bash
streamlit run app.py
```

## 🔑 API Key

This project requires a TMDB API key to fetch movie posters. Get one for free at [themoviedb.org](https://www.themoviedb.org/settings/api) and add it to `app.py`.

## 📸 Demo

<img width="1915" height="861" alt="Screenshot 2026-07-07 082903" src="https://github.com/user-attachments/assets/deaa60d3-a653-47f0-b666-2da7fdf499ba" />
<img width="1912" height="925" alt="Screenshot 2026-07-07 082849" src="https://github.com/user-attachments/assets/62a3c369-0cce-4e62-a4f1-d2a45c398075" />
<img width="1918" height="853" alt="Screenshot 2026-07-07 082917" src="https://github.com/user-attachments/assets/178486a2-d215-474b-8e9e-daacf2b0bf4e" />
<img width="1919" height="849" alt="Screenshot 2026-07-07 082936" src="https://github.com/user-attachments/assets/500bc4d4-b914-42dc-9b67-a8d71884b391" />

## 📄 License

This project is open source and available.
