word = str(input("Type your favourite word: "))
word = word.lower()
new_word = word[::-1]

if new_word == word:
    print("Yay!")
else:
    print("Nope")

