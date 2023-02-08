#By using string methods
word=str(input("Enter the word: "))
print(word[::-1])

#By not using string methods
word=str(input("Enter the word: "))
reverse_word=""
for i in word:
    reverse_word=i+reverse_word
print(reverse_word)