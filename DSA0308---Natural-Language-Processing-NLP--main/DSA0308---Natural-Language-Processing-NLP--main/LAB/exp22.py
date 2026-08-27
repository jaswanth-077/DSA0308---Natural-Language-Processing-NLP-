import spacy

# Load English model
nlp = spacy.load("en_core_web_sm")

# Input text
text = input("Enter a text: ")

doc = nlp(text)

# Pronouns to check
pronouns = {
    "he", "she", "it", "they",
    "him", "her", "them",
    "his", "their", "its"
}

# Store previous noun candidates
noun_candidates = []

print("\nReference Resolution")
print("----------------------------")

for token in doc:

    # Store nouns and proper nouns
    if token.pos_ in ["NOUN", "PROPN"]:
        noun_candidates.append(token.text)

    # Check pronouns
    if token.text.lower() in pronouns:

        if noun_candidates:
            antecedent = noun_candidates[-1]

            print(
                f"{token.text} -> {antecedent}"
            )
        else:
            print(
                f"{token.text} -> No antecedent found"
            )