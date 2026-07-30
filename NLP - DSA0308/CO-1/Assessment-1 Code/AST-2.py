import re
text = """Artificial Intelligence (AI) is transforming industries across the world.
AI is used in healthcare to assist doctors in diagnosis, in banking to detect fraud,
and in education to provide personalized learning experiences.
Many companies invest heavily in AI research because AI improves efficiency
and enables intelligent decision-making. As AI continues to evolve,
professionals with AI skills are in high demand."""
pattern = r"\bAI\b"
match = re.search(pattern, text)
if match:
    print("First Occurrence :", match.group())
    print("Starting Position :", match.start())
    print("Ending Position :", match.end())

    count = len(re.findall(pattern, text))
    print("Total Occurrences :", count)
else:
    print("Word 'AI' not found.")
