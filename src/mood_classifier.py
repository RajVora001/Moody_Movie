mood_to_genre = {
    "happy": ["Comedy", "Family"],
    "sad": ["Drama", "Romance"],
    "angry": ["Action" "Thriller"],
    "joyful": ["Adventure" "Fantasy"],
    "neutral": ["Documentary", "Biography"],
    "anxious": ["Horror", "Mystery"]
}

def classify_by_mood(genre):
    for mood, genres in mood_to_genre.items():
        if any(g in genre for g in genres):
            return mood
    return 'neutral'

