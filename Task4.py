from textblob import TextBlob

# Teksti
sentences = [
    "Šis produkts ir lielisks, esmu ļoti apmierināts!",
    "Esmu vīlies, produkts neatbilst aprakstam.",
    "Neitrāls produkts, nekas īpašs."
]

for sentence in sentences:
    blob = TextBlob(sentence)
    sentiment = blob.sentiment.polarity
    if sentiment > 0:
        print(f"Text: {sentence} - Sentiment: Positive")
    elif sentiment < 0:
        print(f"Text: {sentence} - Sentiment: Negative")
    else:
        print(f"Text: {sentence} - Sentiment: Neutral")
