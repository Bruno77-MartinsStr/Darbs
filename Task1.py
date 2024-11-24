import re
from collections import Counter

text = "Mākoņainā dienā kaķis sēdēja uz palodzes. Kaķis domāja, kāpēc debesis ir pelēkas. Kaķis gribēja redzēt sauli, bet saule slēpās aiz mākoņiem."

text = re.sub(r'[^\w\s]', '', text.lower())
words = text.split()

word_count = Counter(words)
print(word_count)
