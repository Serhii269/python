import string

text = input("Enter the line: ")

for symbol in string.punctuation:
    text = text.replace(symbol, "")

words = text.split()

hashtag = "#"

for word in words:
    hashtag += word.capitalize()

if len(hashtag) > 140:
    hashtag = hashtag[:140]

print(hashtag)
