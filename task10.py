from googletrans import Translator

texts = [
    "Labdien! Kā jums klājas?",
    "Es šodien lasīju interesantu grāmatu."
]

translator = Translator()

for text in texts:
    translated = translator.translate(text, src='lv', dest='en')
    print(f"Original: {text} - Translated: {translated.text}")
