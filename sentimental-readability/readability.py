from cs50 import get_string

userInput = get_string("Text: ")

A = len(userInput)

words = 0
sentences = 0
letters = 0

for i in range(0, A, 1):
    if userInput[i] = " ":
        words += 1
    elif userInput[i] = "." or "?" or "!":
        sentences += 1
    else:
        letters += 1

L = 0
S = 0


calculate = 0.0588 * L - 0.296 * S - 15.8

if calculate >= 16:
    print("Grade 16+")

if calculate < 1:
    print("Before Grade 1")


print(f"Grade {}")