import re

pattern = "[a-zA-Z0-9]+@[a-zA-Z]+\.(com|net|org|ke)"

user_input = input("Enter your email: ")
if(re.search(pattern, user_input)):
    print("Valid email")
else:
    print("Invalid email")