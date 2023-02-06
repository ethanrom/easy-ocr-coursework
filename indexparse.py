import re

with open("input.txt", "r") as file:
    text = file.read()

pattern = r"\b[A-Za-z]{2}\/\d{2}\/\d{5}\b"
match = re.search(pattern, text)

if match:
    index_number = match.group()
    index_number = index_number[0].upper() + index_number[1].upper() + index_number[2:]
    print("index number: " + index_number)
else:
    print("index number not found")
