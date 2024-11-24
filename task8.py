import spacy

nlp = spacy.load("xx_ent_wiki_sm")

text = "Valsts prezidents Egils Levits piedalījās pasākumā, ko organizēja Latvijas Universitāte."

doc = nlp(text)

for ent in doc.ents:
    if ent.label_ == "PERSON":
        print(f"Personvārds: {ent.text}")
    elif ent.label_ == "ORG":
        print(f"Organizācija: {ent.text}")
