import spacy

nlp = spacy.load("en_core_web_sm")

text = input("Enter a text: ")

doc = nlp(text)

pronouns = {
    "he": "male",
    "him": "male",
    "his": "male",
    "she": "female",
    "her": "female",
    "hers": "female",
    "they": "plural",
    "them": "plural",
    "their": "plural"
}

previous_subjects = []

print("\nReference Resolution")
print("----------------------------")

for token in doc:

    # Identify noun/proper-noun subjects
    if token.pos_ in ["NOUN", "PROPN"] and token.dep_ in ["nsubj", "nsubjpass"]:
        previous_subjects.append(token.text)

    # Resolve pronouns
    if token.text.lower() in pronouns:

        if previous_subjects:
            antecedent = previous_subjects[-1]
            print(f"{token.text} -> {antecedent}")
        else:
            print(f"{token.text} -> Unknown")