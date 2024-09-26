def recommend_movies(movies, mood, n=5):
    recommend = movies[movies["mood"] == mood]
    return recommend[['Series_Title', 'Genre', 'IMDB_Rating' 'Released_Year']].head(n)
