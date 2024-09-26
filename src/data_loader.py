import pandas as pd


def load_dataset(filepath):
    return pd.read_csv(filepath)


def preprocess_data(movies):
    movies.dropna(subset=["Series_Title", "Genre", "IMDB_Rating"], inplace=True)
    return movies
