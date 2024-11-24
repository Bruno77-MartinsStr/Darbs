import re

raw_text = "@John: Šis ir lielisks produkts!!! Vai ne? 👏👏👏 http://example.com"

cleaned_text = re.sub(r'[@#\!\?\.\,;:]+', '', raw_text)  
cleaned_text = re.sub(r'http[s]?://\S+', '', cleaned_text)  
cleaned_text = cleaned_text.lower()

print(f"Cleaned text: {cleaned_text}")
