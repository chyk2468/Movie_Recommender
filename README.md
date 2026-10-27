# Movie Recommender

****Discover movies with similar genres, cast, crew, keywords, and plot descriptions.****

[![GitHub](https://img.shields.io/badge/GitHub-Source-24292f?logo=github)](https://github.com/chyk2468/Movie_Recommender)

## 1. Project Title & Tagline

**Discover movies with similar genres, cast, crew, keywords, and plot descriptions.**

## 2. Problem Statement

Discover movies with similar genres, cast, crew, keywords, and plot descriptions.

## 3. Project Preview

No screenshot or GIF is linked yet. Add a real screenshot or short recording of the application here.

[Open the interactive architecture explorer](architecture.html)

## 4. Overview

1. Select a movie by title.
2. Combine metadata such as genres, cast, director, keywords, and overview into a tag string.
3. Convert tags into a CountVectorizer feature matrix.
4. Compute similarity and return the closest titles, excluding the selected film.

## 5. Key Features

- Content-based recommendations from movie metadata.
- Searchable movie selection.
- Ranked results with poster and movie details when available.
- Notebook workflow for data preparation and model construction.

## 6. Architecture / Workflow

![Animated Movie Recommender workflow](docs/readme-architecture.svg)

The moving markers show the system flow. Open the [interactive architecture explorer](architecture.html) to select a stage and read its role.

- Content-based recommendations from movie metadata.
- Searchable movie selection.
- Ranked results with poster and movie details when available.
- Notebook workflow for data preparation and model construction.

## 7. Tech Stack

**Stack:** Python, Pandas, scikit-learn, Streamlit, TMDB 5000 dataset

## 8. Installation & Setup

```bash
git clone https://github.com/chyk2468/Movie_Recommender.git
cd Movie_Recommender
python -m venv .venv
```

Activate the environment and install dependencies:

```bash
pip install -r requirements.txt
```

Follow the model-preparation steps in `Movie_Recommender.ipynb` if the required artefacts are not present, then launch:

```bash
streamlit run app.py
```

## 9. Usage

```bash
git clone https://github.com/chyk2468/Movie_Recommender.git
cd Movie_Recommender
python -m venv .venv
```

Activate the environment and install dependencies:

```bash
pip install -r requirements.txt
```

Follow the model-preparation steps in `Movie_Recommender.ipynb` if the required artefacts are not present, then launch:

```bash
streamlit run app.py
```

## 10. Project Structure

| File | Purpose |
| --- | --- |
| `app.py` | Recommendation interface |
| `Movie_Recommender.ipynb` | Data preparation and model workflow |
| `tmdb_5000_movies.csv` | Movie metadata |
| `tmdb_5000_credits.csv` | Cast and crew metadata |

## 11. Results & Demo

No verified benchmark or hosted demo is specified here. Run the project and add representative outputs, evaluation metrics, and a screenshot or GIF.

## 12. Future Enhancements

- Add automated tests for the main workflow and edge cases.
- Improve validation and error handling.
- Record reproducible evaluation results.
- Add a short demo GIF or screenshots.

## 13. License

Add a `LICENSE` file if you intend to grant permissions for reuse or redistribution.
