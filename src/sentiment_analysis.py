from textblob import TextBlob

def get_sentiment(description):
    analysis = TextBlob(description)
    return analysis.sentiment.polarity

