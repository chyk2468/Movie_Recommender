<div align="center">

# 🎬 Movie Recommender System

### Content-Based Filtering · TMDB 5000 Dataset · Streamlit

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org)
[![TMDB](https://img.shields.io/badge/Dataset-TMDB_5000-01b4e4?style=for-the-badge)](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)
[![License](https://img.shields.io/badge/License-Educational-22c55e?style=for-the-badge)](#-license)

> A smart **movie recommendation engine** that suggests films you'll actually enjoy —  
> powered by **cosine similarity** on cast, crew, genres, keywords, and plot tags  
> from the **TMDB 5000 Movies Dataset**.

</div>

---

## ✨ Features

| Feature | Details |
|---|---|
| 🎯 **Content-Based Filtering** | Recommendations based on genres, cast, crew & plot |
| 🔢 **5000-Feature Vectorisation** | `CountVectorizer` bag-of-words + Porter stemming |
| 📐 **Cosine Similarity** | Accurate similarity scores across all ~4800 movies |
| 🖥️ **Interactive Streamlit UI** | Dropdown search, top-5 grid with posters & ratings |
| 📅 **Movie Details** | Shows release year and TMDB rating per recommendation |
| 📦 **Large Coverage** | TMDB 5000 movies — broad genre and era coverage |

---

## 🏗️ How It Works

```
User selects a movie
        │
        ▼
┌───────────────────────────┐
│   Data Preprocessing       │  ← merge movies + credits CSVs
│   Extract: genres, cast,   │  ← top 3 cast + director
│   crew, keywords, overview │  ← lowercase + Porter stemming
└────────────┬──────────────┘
             │  Combined "tags"
             ▼
┌───────────────────────────┐
│   CountVectorizer          │  ← 5000 features, English stop words removed
│   Bag-of-Words Matrix      │
└────────────┬──────────────┘
             │
             ▼
┌───────────────────────────┐
│   Cosine Similarity Matrix │  ← every movie vs every movie
└────────────┬──────────────┘
             │  Top-5 nearest neighbours (excluding selected)
             ▼
      5 Movie Recommendations
   (title · poster · year · rating)
```

---

## 📊 Dataset

**[TMDB 5000 Movie Metadata](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)**

| File | Description |
|---|---|
| `tmdb_5000_movies.csv` | Titles, overviews, genres, keywords, ratings |
| `tmdb_5000_credits.csv` | Full cast and crew per movie |

---

## 📁 Project Structure

```
Movie_Recommender/
│
├── app.py                    # Streamlit web application
├── Movie_Recommender.ipynb   # Data processing & model building notebook
│
├── tmdb_5000_movies.csv      # TMDB movies dataset
├── tmdb_5000_credits.csv     # TMDB credits dataset
│
├── movies.pkl                # Processed movie data with tags  (generated)
├── similarity.pkl            # Cosine similarity matrix        (generated)
│
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

> ⚠️ `movies.pkl` and `similarity.pkl` are **generated** by running the notebook. They are not included in the repo.

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| **Web UI** | [Streamlit](https://streamlit.io/) |
| **Data Manipulation** | [pandas](https://pandas.pydata.org/), [numpy](https://numpy.org/) |
| **ML / Similarity** | [scikit-learn](https://scikit-learn.org/) — `CountVectorizer`, `cosine_similarity` |
| **NLP** | [NLTK](https://www.nltk.org/) — `PorterStemmer` |
| **HTTP** | [requests](https://requests.readthedocs.io/) |

---

## ⚙️ Setup & Installation

### 1. Clone the Repository

```bash
git clone https://github.com/chyk2468/Movie_Recommender.git
cd Movie_Recommender
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Download NLTK Data

```python
import nltk
nltk.download('punkt')
```

### 4. Build the Model

Open and run **all cells** in `Movie_Recommender.ipynb`:

```bash
jupyter notebook Movie_Recommender.ipynb
```

This will:
- Merge and preprocess TMDB datasets
- Build the 5000-feature cosine similarity matrix
- Save `movies.pkl` and `similarity.pkl`

### 5. Launch the App

```bash
streamlit run app.py
```

Open your browser at **`http://localhost:8501`**

---

## 🖥️ Usage

1. Select a movie from the **dropdown search box**
2. Click **Show Recommendation**
3. View your **Top 5 recommended movies** with:
   - 🎞️ Movie poster
   - 📅 Release year
   - ⭐ TMDB rating

---

## 🧠 Algorithm Details

### Text Preprocessing
```
genres + keywords + top-3 cast + director + overview
        │
        ▼
  lowercase → remove spaces → Porter stemming
        │
        ▼
  Single combined "tags" string per movie
```

### Feature Extraction
- `CountVectorizer(max_features=5000, stop_words='english')`
- Produces a sparse matrix of shape `(~4800, 5000)`

### Similarity Calculation
- **Cosine similarity**: measures the angle between two tag vectors
- Score range: `0.0` (no similarity) → `1.0` (identical)
- Top-5 most similar titles returned (excluding the selected movie itself)

---

## 🔧 Customisation

```python
# Change number of features
CountVectorizer(max_features=10000)

# Change number of recommendations (app.py)
distances[1:11]  # top 10 instead of 5

# Add more tags
tags = genres + keywords + cast + crew + overview + production_companies
```

---

## ❗ Troubleshooting

| Issue | Fix |
|---|---|
| `FileNotFoundError: movies.pkl` | Run `Movie_Recommender.ipynb` first |
| `LookupError: punkt` | Run `nltk.download('punkt')` |
| Memory issues | Reduce `max_features` or use a machine with ≥4 GB RAM |
| Slow loading | The similarity matrix is large (~180 MB) — normal on first load |

---

## 🚀 Future Enhancements

- [ ] 🔗 Live poster fetching via TMDB API
- [ ] 👥 Collaborative filtering (user-based)
- [ ] 🔀 Hybrid recommendation (content + collaborative)
- [ ] ⭐ User rating & feedback integration
- [ ] 🔍 Advanced NLP — TF-IDF, word embeddings
- [ ] 🎭 Genre filter and year range selector

---

## 📜 License

This project is built for **educational purposes**.  
The TMDB dataset is used under [TMDB's terms of use](https://www.themoviedb.org/terms-of-use).

---

<div align="center">

Made with ❤️ by **Ch. Yashwant Kumar**

[![GitHub](https://img.shields.io/badge/GitHub-chyk2468-181717?style=flat-square&logo=github)](https://github.com/chyk2468)

⭐ If you found this useful, please consider starring the repo!

</div>
