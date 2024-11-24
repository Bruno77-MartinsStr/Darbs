from langdetect import detect

texts = [
    "Šodien ir saulaina diena.",
    "Today is a sunny day."
]

for text in texts:
    try:
        language = detect(text)
        print(f"Text: {text} - Language: {language}")
    except Exception as e:
        print(f"Error: {e} for text: {text}")
