from transformers import pipeline

# Izveido rezumēšanas cauruli, izmantojot BART modeli
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# Teksts
text = """
Latvija ir valsts Baltijas reģionā. Tās galvaspilsēta ir Rīga, kas ir slavena ar savu vēsturisko centru un skaistajām ēkām. Latvija robežojas ar Lietuvu, Igauniju un Krieviju, kā arī tai ir piekļuve Baltijas jūrai. Tā ir viena no Eiropas Savienības dalībvalstīm.
"""

# Rezumēšana
summary = summarizer(text, max_length=100, min_length=50, do_sample=False)

# Rezultāts
print("Rezumē:", summary[0]['summary_text'])
