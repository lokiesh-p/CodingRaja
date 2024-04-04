def is_palindrome(word):
    return word == word[::-1]

word = input("Enter a word: ")
if is_palindrome(word):
    print("Yes, it's a palindrome.")
else:
    print("No, it's not a palindrome.")
