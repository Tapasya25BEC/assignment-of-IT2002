text = input("Enter a string: ")

print("Number of characters:", len(text))

vowels = 0
consonants = 0
for ch in text.lower():
    if ch.isalpha():
        if ch in "aeiou":
            vowels += 1
        else:
            consonants += 1

print("Vowels:", vowels)
print("Consonants:", consonants)

reversed_text = text[::-1]
print("Reversed string:", reversed_text)

if text.lower() == reversed_text.lower():
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
