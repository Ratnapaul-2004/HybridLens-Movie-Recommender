# HybridLens-Movie-Recommender

🎬 HybridLens: Movie Recommendation System
A hybrid movie recommendation engine that intelligently combines content-based filtering and collaborative filtering to deliver highly accurate and personalized movie suggestions.

🚀 Features
- 🔍 Hybrid Recommendation Engine
  Uses TMDB metadata + user similarity (collaborative filtering).

- 🎞 Content-Based Filtering
  Uses movie genres, keywords, cast, crew & overview.

- 👥 Collaborative Filtering
  Utilizes user ratings and similarity (cosine similarity).

- ⚡ Optimized ML Pipeline
  Includes preprocessing, vectorization, similarity matrix creation, and caching.

- 🧩 Deployable Compatibility
  Supports saving/loading models (similarity.pkl, movie_list.pkl, etc.)

🛠 Tech Stack
- Python

- Pandas, NumPy

- Scikit-learn

- Pickle for saving models

- Jupyter Notebook for development

- Git & GitHub for version control

📂 Project Structure

HybridLens-Movie-Recommender/
│── data/
│   ├── tmdb_5000_movies.csv
│   ├── tmdb_5000_credits.csv
│── models/
│   ├── similarity.pkl
│   ├── movies.pkl
│── notebook/
│   ├── HybridLens Recommender.ipynb
│── .gitignore
│── README.md
│── app.py       (if deployed)

▶️ How It Works

1. Preprocess data

  - Merge movie & credits data
  
  - Extract important features
  
  - Tokenize & vectorize text features

2. Compute similarity matrix

  - Cosine similarity on feature vectors
  
  - Saved as similarity.pkl

3. Recommend movies

  - Find top similar movies
  
  - Display titles/posters

📦 Installation

```git clone https://github.com/Ratnapaul-2004/HybridLens-Movie-Recommender.git
cd HybridLens-Movie-Recommender
pip install -r requirements.txt
```

🧪 Usage

Running the Jupyter Notebook

`jupyter notebook`

Running your Streamlit App

`streamlit run app.py`

🎯 Future Improvements

- Add user login & personalized history

- Deploy as Streamlit or Flask web app

- Add real-time search and auto-suggest

- Integrate movie posters from TMDB API

Made with ❤️ 
