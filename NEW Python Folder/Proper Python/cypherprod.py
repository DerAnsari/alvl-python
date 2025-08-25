import random
import string

char = " " + string.punctuation + string.digits + string.ascii_letters
char = list(char)
key = char.copy()

random.shuffle(key)

print(char)
print(key)

#Encrypt
text = input("Enter encrypt msg")
cypher = ""

for letter in text:
    index = char.index(letter)
    cypher += key[index]

print(f"encrypted text= {cypher}")

#Decrypt
text = ""
cypher = input("Enter encrypt msg")

for letter in cypher:
    index = key.index(letter)
    text += char[index]

print(f"decrypted text= {text}")