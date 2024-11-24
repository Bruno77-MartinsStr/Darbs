import spacy

nlp = spacy.load("xx_ent_wiki_sm")

words = ["māja", "dzīvoklis", "jūra"]

vectors = [nlp(word).vector for word in words]

def similarity(word1, word2):
    return nlp(word1).similarity(nlp(word2))

for i in range(len(words)):
    for j in range(i+1, len(words)):
        word1 = words[i]
        word2 = words[j]
        sim = similarity(word1, word2)
        print(f"Semantiskā līdzība starp '{word1}' un '{word2}': {sim:.4f}")
