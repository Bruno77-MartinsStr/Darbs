from fuzzywuzzy import fuzz

text1 = "Rudens lapas ir dzeltenas un oranžas. Lapas klāj zemi un padara to krāsainu."
text2 = "Krāsainas rudens lapas krīt zemē. Lapas ir oranžas un dzeltenas."

similarity_percentage = fuzz.ratio(text1, text2)

print(f"Similarity: {similarity_percentage}%")
