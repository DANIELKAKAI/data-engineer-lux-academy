import pandas as pd

from textblob import TextBlob


def get_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    print(sentiment)
    return sentiment


df = pd.read_csv('Week 5 Assignment/training.1600000.processed.noemoticon.csv',
                 sep=",",
                 encoding="ISO-8859-1",
                 names=["target", "ids", "date", "flag", "user", "text"])


df = df.assign(sentimental_score = get_sentiment(str(df['text'])))


