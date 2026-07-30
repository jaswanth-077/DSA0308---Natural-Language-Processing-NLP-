import re
email = "john.doe123@gmail.com"
mobile = "+91-9876543210"
password = "P@ssw0rd123"
dob = "15/08/2004"
reg_no = "23AIML1056"
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
mobile_pattern = r'^\+91-[6-9]\d{9}$'
password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@#$%&!*])[A-Za-z\d@#$%&!*]{8,}$'
dob_pattern = r'^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}$'
reg_pattern = r'^\d{2}[A-Z]{4}\d{4}$'
print("Email:", "Valid" if re.fullmatch(email_pattern, email) else "Invalid")
print("Mobile:", "Valid" if re.fullmatch(mobile_pattern, mobile) else "Invalid")
print("Password:", "Valid" if re.fullmatch(password_pattern, password) else "Invalid")
print("Date of Birth:", "Valid" if re.fullmatch(dob_pattern, dob) else "Invalid")
print("Register Number:", "Valid" if re.fullmatch(reg_pattern, reg_no) else "Invalid")
