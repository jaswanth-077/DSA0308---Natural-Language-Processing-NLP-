import re
email_pattern = re.compile(
    r'^[a-zA-Z0-9]+[a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.(com|org|edu|in)$'
)
emails = [
    "john@gmail.com",
    "student123@yahoo.org",
    "abc@college.edu",
    "test_user@domain.in",
    "invalid@email",
    "@gmail.com"
]
for email in emails:
    if email_pattern.fullmatch(email):
        print(email, "-> Valid Email")
    else:
        print(email, "-> Invalid Email")
