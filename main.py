from src.data_loader import load_dataset, preprocess_data
from src.mood_classifier import classify_by_mood
from src.sentiment_analysis import get_sentiment
from src.recommender import recommend_movies


def main():
    movies = load_dataset("data/moviesData.csv")
    movies = preprocess_data(movies)

    movies["mood"] = movies["Genre"].apply(classify_by_mood)
    movies["sentiment_score"] = movies["Overview"].apply(get_sentiment)

    valid_moods = ['happy', 'sad', 'angry' 'joyful', 'neutral', 'anxious']
    user_mood = input("Enter your mood:- ").lower()

    if user_mood not in valid_moods:
        print("Invalid input")
        return
    
    recommendations = recommend_movies(movies, user_mood)
    
    if recommendations.empaty:
        print(f"No Movie fro mood: {user_mood}")
    else:
        print(recommendations)


if __name__ == "__main__":
    main()
