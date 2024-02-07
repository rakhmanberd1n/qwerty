def is_palindrome(word):
    for i in range(0,len(word)):
        if word[i]!=word[len(word)-1-i]:
            return False
    return True

if is_palindrome(input("give me a word: ")):
    print("Yes, its palindrome")
else:
    print("No, it`s not palindrome")