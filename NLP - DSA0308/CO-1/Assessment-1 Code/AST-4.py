import re
email = input("Enter Email ID: ")
password = input("Enter Password: ")
email_pattern = r'^[a-zA-Z0-9]+[a-zA-Z0-9._%+-]*@[a-zA-Z0-9.-]+\.(com|org|edu|in)$'
password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%&!*])[^\s]{8,}$'
if re.fullmatch(email_pattern, email):
    print("Valid Email ID")
else:
    print("Invalid Email ID")
if re.fullmatch(password_pattern, password):
    print("Strong Password")
else:
    print("Weak Password")
