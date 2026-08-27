import spacy
import nltk
from nltk.corpus import wordnet

# Download WordNet
nltk.download("wordnet")
nltk.download("omw-1.4")

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Input sentence
sentence = input("Enter a sentence: ")

# Process sentence
doc = nlp(sentence)

print("\nNoun Phrases and Meanings")
print("----------------------------")

for chunk in doc.noun_chunks:

    phrase = chunk.text

    # Find the main noun/root of the phrase
    root_word = chunk.root.text

    # Get WordNet meanings
    synsets = wordnet.synsets(root_word)

    print("\nNoun Phrase:", phrase)
    print("Main Noun:", root_word)

    if synsets:
        print("Meaning:", synsets[0].definition())
    else:
        print("Meaning: Not found in WordNet")