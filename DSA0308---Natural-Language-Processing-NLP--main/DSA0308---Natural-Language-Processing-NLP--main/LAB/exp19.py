import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize

# Download required WordNet resources
nltk.download("wordnet")
nltk.download("omw-1.4")
nltk.download("punkt")

# Lesk Algorithm
def simple_lesk(sentence, word):

    # Tokenize and convert to lowercase
    tokens = word_tokenize(sentence.lower())

    # Context words excluding the target word
    context = set(tokens)
    context.discard(word.lower())

    # Get all possible senses
    synsets = wordnet.synsets(word)

    best_synset = None
    best_score = 0

    # Compare every sense with the context
    for synset in synsets:

        # Get definition
        definition = synset.definition().lower()

        # Get example sentences
        examples = " ".join(synset.examples()).lower()

        # Combine definition and examples
        sense_text = definition + " " + examples

        # Tokenize sense description
        sense_words = set(word_tokenize(sense_text))

        # Calculate overlap
        overlap = context.intersection(sense_words)

        score = len(overlap)

        print("\nSense:", synset.name())
        print("Definition:", synset.definition())
        print("Overlap:", overlap)
        print("Score:", score)

        # Select best sense
        if score > best_score:
            best_score = score
            best_synset = synset

    return best_synset


# Main Program
sentence = input("Enter a sentence: ").lower()
word = input("Enter the ambiguous word: ").lower()

result = simple_lesk(sentence, word)

print("\n-----------------------------")
print("Sentence:", sentence)
print("Word:", word)

if result:
    print("Predicted Sense:", result.name())
    print("Meaning:", result.definition())
else:
    print("No suitable sense found.")

print("-----------------------------")